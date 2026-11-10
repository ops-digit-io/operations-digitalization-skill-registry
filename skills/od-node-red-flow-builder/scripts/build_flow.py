#!/usr/bin/env python3
"""
build_flow.py - generate a standardized DATATRON rule-engine Node-RED flow.

Usage:
    python3 build_flow.py spec.json output_flow.json

The spec describes inputs (source datapoints), one output (virtual datapoint),
the MQTT topics and the calculation. See SKILL.md -> "Spec format" for details.

The generated flow always follows the house standard:
  config flow  ->  mqtt in / decode / filter uuids / split / convert sysTime
  -> per-input switch + change (store latest value in flow context)
  -> calculate <Output> (function)  -> [filter on change] -> format msg.payload
  -> prepare for protob encoding -> [intervaltime heartbeat]
  -> convert sysTime back -> encode -> mqtt out
  + catch/error logging group, optional cron reset, optional lookup table.
"""
import json, re, secrets, sys

UUID_RE = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
VALUE_FIELDS = ("valueInteger", "valueDouble", "valueBool", "valueString")

# Config-node ids used across the existing plant flows. Re-using them means an
# import binds to the broker / proto file that already exist on the instance.
DEFAULT_BROKER_ID = "a5b9953ab68b73bb"
DEFAULT_PROTO_ID = "7a49aef9.46452"


def nid():
    return secrets.token_hex(8)


def fail(msg):
    sys.exit(f"SPEC ERROR: {msg}")


def validate(spec):
    for k in ("tabLabel", "inputTopic", "inputs", "output", "calc"):
        if k not in spec:
            fail(f"missing '{k}'")
    if not spec["inputs"]:
        fail("at least one input is required")
    names = set()
    for i in spec["inputs"]:
        for k in ("name", "uuid", "field"):
            if k not in i:
                fail(f"input {i} missing '{k}'")
        if not re.match(r"^[A-Za-z][A-Za-z0-9]*$", i["name"]):
            fail(f"input name '{i['name']}' must be alphanumeric (used in flow variable names)")
        if i["name"] in names:
            fail(f"duplicate input name {i['name']}")
        names.add(i["name"])
        if not UUID_RE.match(i["uuid"]):
            fail(f"input {i['name']} uuid '{i['uuid']}' is not a valid UUID")
        if i["field"] not in VALUE_FIELDS:
            fail(f"input {i['name']} field must be one of {VALUE_FIELDS}")
    o = spec["output"]
    for k in ("name", "uuid", "field"):
        if k not in o:
            fail(f"output missing '{k}'")
    if not UUID_RE.match(o["uuid"]):
        fail(f"output uuid '{o['uuid']}' is not a valid UUID")
    if o["field"] not in VALUE_FIELDS:
        fail(f"output field must be one of {VALUE_FIELDS}")
    if o["uuid"] in {i["uuid"] for i in spec["inputs"]}:
        fail("output uuid must not be one of the input uuids (would create a feedback loop)")
    opts = spec.get("options", {})
    if opts.get("evaluate", "perBatch") not in ("perBatch", "perPacket"):
        fail("options.evaluate must be 'perBatch' or 'perPacket'")


def derive_output_topic(t):
    # Default: same topic the data came from, without MQTT wildcards.
    return re.sub(r"/[#+]$", "", t)


def build(spec):
    validate(spec)
    opts = spec.get("options", {})
    evaluate = opts.get("evaluate", "perBatch")
    heartbeat = opts.get("heartbeatMinutes", 0)
    on_change = opts.get("publishOnChangeOnly", True)
    resets = opts.get("resetCrons", [])
    lookup = opts.get("lookupTable")
    broker_id = spec.get("brokerId", DEFAULT_BROKER_ID)
    proto_id = spec.get("protoFileId", DEFAULT_PROTO_ID)
    out_topic = spec.get("outputTopic") or derive_output_topic(spec["inputTopic"])
    machine = spec.get("machineName", "")
    inputs = spec["inputs"]
    out = spec["output"]
    ovar = "datapoint" + out["name"]

    TAB = nid()
    nodes, groups = [], []

    def add(n, x, y):
        n.setdefault("id", nid())
        n["z"], n["x"], n["y"] = TAB, x, y
        nodes.append(n)
        return n

    def group(name, members, color=None):
        xs = [m["x"] for m in members]
        ys = [m["y"] for m in members]
        g = {"id": nid(), "type": "group", "z": TAB, "name": name,
             "style": {"label": True}, "nodes": [m["id"] for m in members],
             "x": min(xs) - 110, "y": min(ys) - 50,
             "w": max(xs) - min(xs) + 240, "h": max(ys) - min(ys) + 90}
        for m in members:
            m["g"] = g["id"]
        groups.append(g)

    def fn(name, code, wires, info=""):
        n = {"type": "function", "name": name, "func": code, "outputs": 1,
             "noerr": 0, "initialize": "", "finalize": "", "libs": [], "wires": wires}
        if info:
            n["info"] = info
        return n

    def change(name, rules, wires):
        return {"type": "change", "name": name, "rules": rules, "action": "", "property": "",
                "from": "", "to": "", "reg": False, "wires": wires}

    def debug(name, active=False, complete="true"):
        return {"type": "debug", "name": name, "active": active, "tosidebar": True, "console": False,
                "tostatus": False, "complete": complete,
                "targetType": "full" if complete == "true" else "msg",
                "statusVal": "", "statusType": "auto", "wires": []}

    def link_pair(xo, yo, xi, yi, name):
        lo = add({"type": "link out", "name": f"{name} out", "mode": "link", "links": [], "wires": []}, xo, yo)
        li = add({"type": "link in", "name": f"{name} in", "links": [lo["id"]], "wires": [[]]}, xi, yi)
        lo["links"] = [li["id"]]
        return lo, li

    # ------------------------------------------------------------------ config
    cfg_rules = [{"t": "set", "p": "machineName", "pt": "flow", "to": machine, "tot": "str"}]
    for i in inputs:
        cfg_rules.append({"t": "set", "p": "datapoint" + i["name"], "pt": "flow", "to": i["uuid"], "tot": "str"})
    cfg_rules.append({"t": "set", "p": ovar, "pt": "flow", "to": out["uuid"], "tot": "str"})
    filter_list = ", ".join(f"flow.get('datapoint{i['name']}')" for i in inputs)
    dbg_keys = ",\n".join(f"    datapoint{i['name']}: flow.get('datapoint{i['name']}')" for i in inputs)

    cfg_dbg = add(debug("flow config", active=True), 900, 80)
    cfg_dbgfn = add(fn("Debug flow config",
        "var payload = {\n    machineName: flow.get('machineName'),\n" + dbg_keys +
        f",\n    {ovar}: flow.get('{ovar}'),\n    datapointConfigFilter: flow.get('datapointConfigFilter')\n}};\n\n"
        "return {\n    payload: payload,\n    debugInfo: \"Added flow configuration\"\n};",
        [[cfg_dbg["id"]]]), 700, 80)
    cfg_filter = add(fn("set datapointConfigFilter",
        f"const uuids = [{filter_list}];\n\nflow.set('datapointConfigFilter', uuids);\n\nreturn msg;",
        [[cfg_dbgfn["id"]]]), 490, 80)
    cfg_set = add(change("Set flow config", cfg_rules, [[cfg_filter["id"]]]), 290, 80)
    cfg_inj = add({"type": "inject", "name": "Trigger once", "props": [{"p": "payload"}, {"p": "topic", "vt": "str"}],
                   "repeat": "", "crontab": "", "once": True, "onceDelay": "0", "topic": "", "payload": "",
                   "payloadType": "date", "wires": [[cfg_set["id"]]]}, 110, 80)
    cfg_members = [cfg_inj, cfg_set, cfg_filter, cfg_dbgfn, cfg_dbg]

    # optional lookup table (template -> csv -> flow.lookupTable), same as BLM / Line15 flows
    if lookup:
        cols = lookup.get("columns", ["key", "value"])
        sep = lookup.get("separator", ";")
        lk_store = add(change("move to flow variable",
                              [{"t": "set", "p": "lookupTable", "pt": "flow", "to": "payload", "tot": "msg"}], [[]]), 700, 140)
        lk_csv = add({"type": "csv", "name": "csv parsing", "sep": "\\t" if sep == "\t" else sep, "hdrin": False,
                      "hdrout": "none", "multi": "mult", "ret": "\\n", "temp": ",".join(cols), "skip": "0",
                      "strings": True, "include_empty_strings": "", "include_null_values": "",
                      "wires": [[lk_store["id"]]]}, 490, 140)
        lk_tpl = add({"type": "template", "name": "mapping table", "field": "payload", "fieldType": "msg",
                      "format": "text", "syntax": "plain", "template": lookup["rows"].strip("\n"), "output": "str",
                      "wires": [[lk_csv["id"]]]}, 290, 140)
        cfg_inj["wires"][0].append(lk_tpl["id"])
        cfg_members += [lk_tpl, lk_csv, lk_store]
    group("config flow", cfg_members)

    # optional cron reset of calculation state (e.g. shift counters)
    if resets:
        rs_dbg = add(debug("state reset"), 700, 230)
        rs_chg = add(change("reset calculation state",
                            [{"t": "delete", "p": "ruleState", "pt": "flow"}], [[rs_dbg["id"]]]), 450, 230)
        rs_members = [rs_chg, rs_dbg]
        for k, cron in enumerate(resets):
            rs_members.append(add({"type": "inject", "name": f"reset {cron}",
                                   "props": [{"p": "payload"}, {"p": "topic", "vt": "str"}], "repeat": "",
                                   "crontab": cron, "once": False, "onceDelay": 0.1, "topic": "", "payload": "",
                                   "payloadType": "date", "wires": [[rs_chg["id"]]]}, 160, 230 + k * 50))
        group("reset calculation state (cron, UTC of the node-red container)", rs_members)

    # ------------------------------------------------------------- input chain
    Y = 360 + (len(resets) * 50 if resets else 0)
    lo_in, li_in = link_pair(1170, Y, 110, Y + 140, "decoded packets")
    conv = add(fn("Convert sysTime (UTC timestamp)",
        "var sysTime = msg.payload.sysTime\n\n"
        "const seconds_epoch = Number(BigInt(sysTime) >> 32n) // high 32 bit: seconds since epoch\n"
        "const nanos = Number(BigInt(sysTime) & 0xFFFFFFFFn)  // low 32 bit: nanoseconds\n"
        "const millis = Math.round(nanos / 1e6)\n"
        "const millis_epoch = seconds_epoch * 1000 + millis // UTC\n\n"
        "msg.payload.sysTime = millis_epoch\n\nreturn msg;", [[lo_in["id"]]]), 960, Y)
    split = add({"type": "split", "name": "flatten PLCPacket Array", "splt": "\\n", "spltType": "str",
                 "arraySplt": 1, "arraySpltType": "len", "stream": False, "addname": "",
                 "wires": [[conv["id"]]]}, 740, Y)
    filt = add(fn("filter uuids",
        "// get flow variable\nconst uuids = flow.get('datapointConfigFilter') || [];\n\n"
        "// filter for uuid\nconst results = msg.payload.plcPackets.filter(plcPacket => uuids.includes(plcPacket.uuid));\n\n"
        "// nothing relevant in this batch\nif (results.length === 0) {\n    return null;\n}\n\n"
        "// publish results\nmsg.payload = results;\n\nreturn msg;",
        [[split["id"]]],
        info="1. loop over msg.payload.plcPackets\n2. keep only packets whose uuid is in datapointConfigFilter\n3. emit the array of matching plcPackets"),
        550, Y)
    dec = add({"type": "decode", "name": "DecodeProto", "protofile": proto_id, "protoType": "PLCPacketList",
               "wires": [[filt["id"]]]}, 370, Y)
    mqin = add({"type": "mqtt in", "name": "", "topic": spec["inputTopic"], "qos": "0", "datatype": "auto-detect",
                "broker": broker_id, "nl": False, "rap": True, "rh": 0, "inputs": 0, "wires": [[dec["id"]]]}, 160, Y)
    group("mqtt connection and message decoding", [mqin, dec, filt, split, conv, lo_in])

    # --------------------------------------------------- store latest values
    Y2 = Y + 140
    sw_rules = [{"t": "eq", "v": "datapoint" + i["name"], "vt": "flow"} for i in inputs]
    lo_calc, li_calc = link_pair(900, Y2 + 30 * (len(inputs) - 1), 110, Y2 + 60 * len(inputs) + 120, "stored value")
    stores = []
    for k, i in enumerate(inputs):
        stores.append(add(change(f"value for {i['name']}", [
            {"t": "set", "p": "value" + i["name"], "pt": "flow", "to": "payload." + i["field"], "tot": "msg"},
            {"t": "set", "p": "time" + i["name"], "pt": "flow", "to": "payload.sysTime", "tot": "msg"}],
            [[lo_calc["id"]]]), 640, Y2 + k * 60))
    sw = add({"type": "switch", "name": "uuid filter per input", "property": "payload.uuid", "propertyType": "msg",
              "rules": sw_rules, "checkall": "false", "repair": False, "outputs": len(inputs),
              "wires": [[s["id"]] for s in stores]}, 360, Y2 + 30 * (len(inputs) - 1))
    li_in["wires"] = [[sw["id"]]]
    group("set message filters and remember latest values", [li_in, sw, lo_calc] + stores)

    # ------------------------------------------------------------ calculation
    Y3 = Y2 + 60 * len(inputs) + 120
    conv_js = {"valueInteger": "toNum(raw)", "valueDouble": "toNum(raw)",
               "valueBool": "(raw === true || raw === 'true')", "valueString": "String(raw)"}
    v_lines = "\n".join(
        f"raw = flow.get('value{i['name']}');\n"
        f"v.{i['name']} = (raw === undefined || raw === null) ? undefined : {conv_js[i['field']]};\n"
        f"t.{i['name']} = flow.get('time{i['name']}');" for i in inputs)
    name_map = ", ".join(f"[flow.get('datapoint{i['name']}')]: '{i['name']}'" for i in inputs)
    batch_guard = ("// evaluate once per decoded batch, after ALL packets of the batch were stored\n"
                   "// (prevents mixing a new value with a stale one, e.g. base/exponent decade jumps)\n"
                   "if (msg.parts && msg.parts.index < msg.parts.count - 1) {\n    return null;\n}\n\n") \
        if evaluate == "perBatch" else "// perPacket: evaluated for every relevant packet (events, counters, triggers)\n\n"
    user_calc = "    " + spec["calc"].strip().replace("\n", "\n    ")
    calc_code = (
        batch_guard +
        "const toNum = x => (typeof x === 'string' ? Number(x) : x);  // int64 arrives as string\n"
        "let raw;\n"
        "const v = {};   // latest value per input (typed)\n"
        "const t = {};   // sysTime (unix ms) of the latest value per input\n" +
        v_lines + "\n\n"
        f"const names = {{{name_map}}};\n"
        "const trigger = msg.payload;                    // packet that caused this evaluation\n"
        "const triggerName = names[trigger.uuid];        // its input name\n"
        "const state = flow.get('ruleState') || {};      // persistent calculation state (reset by cron if configured)\n"
        "const lookup = flow.get('lookupTable') || [];   // optional mapping table\n\n"
        "// ---------------- calculation ----------------\n"
        "const result = (function () {\n" + user_calc + "\n})();\n"
        "// ---------------------------------------------\n\n"
        "flow.set('ruleState', state);\n\n"
        "if (result === undefined || result === null || (typeof result === 'number' && !Number.isFinite(result))) {\n"
        "    return null;\n}\n\n"
        f"msg.payload = {{ {out['field']}: result }};\nreturn msg;")
    Xc = 110
    li_calc["x"], li_calc["y"] = Xc, Y3
    calc_dbg = add(debug(f"{out['name']} result", active=True, complete="payload"), 620, Y3 + 60)
    calc = add(fn(f"calculate {out['name']}", calc_code, [[]],
                  info=spec.get("description", "")), 350, Y3)
    li_calc["wires"] = [[calc["id"]]]
    calc_members = [li_calc, calc, calc_dbg]
    lo_fmt, li_fmt = link_pair(900, Y3, 110, Y3 + 140, "result")
    if on_change:
        rbe = add({"type": "rbe", "name": "filter on change", "func": "rbe", "gap": "", "start": "", "inout": "out",
                   "septopics": False, "property": f"payload.{out['field']}", "topi": "topic",
                   "wires": [[lo_fmt["id"]]]}, 640, Y3)
        calc["wires"] = [[rbe["id"], calc_dbg["id"]]]
        calc_members.append(rbe)
    else:
        calc["wires"] = [[lo_fmt["id"], calc_dbg["id"]]]
    calc_members.append(lo_fmt)
    group(f"calculate {out['name']}", calc_members)

    # ---------------------------------------------- prepare / encode / publish
    Y4 = Y3 + 140
    mqout = add({"type": "mqtt out", "name": "", "topic": out_topic, "qos": "", "retain": "", "respTopic": "",
                 "contentType": "", "userProps": "", "correl": "", "expiry": "", "broker": broker_id,
                 "wires": []}, 1450, Y4)
    enc_dbg = add(debug("encoded message"), 1450, Y4 + 60)
    enc = add({"type": "encode", "name": "EncodeProto", "protofile": proto_id, "protoType": "PLCPacketList",
               "wires": [[mqout["id"], enc_dbg["id"]]]}, 1260, Y4)
    back = add(fn("Convert sysTime back (UTC timestamp)",
        "const dt_new = new Date()\nconst dt = dt_new.getTime()\n\n"
        "// floor, not round: rounding would push the timestamp up to 1 s into the future\n"
        "const seconds = Math.floor(dt / 1000)\n"
        "const nanos = BigInt(seconds) << 32n | BigInt(dt_new.getMilliseconds() * 1e6)\n\n"
        "msg.payload.plcPackets[0].sysTime = Number(nanos)\nreturn msg;", [[enc["id"]]]), 1030, Y4)
    prep = add(change("prepare for protob encoding", [
        {"t": "delete", "p": "parts", "pt": "msg"}, {"t": "delete", "p": "protobufType", "pt": "msg"},
        {"t": "delete", "p": "topic", "pt": "msg"}, {"t": "delete", "p": "qos", "pt": "msg"},
        {"t": "delete", "p": "retain", "pt": "msg"},
        {"t": "move", "p": "payload", "pt": "msg", "to": "payload.plcPackets[0]", "tot": "msg"},
        {"t": "delete", "p": "_msgid", "pt": "msg"}], [[back["id"]]]), 580, Y4)
    if heartbeat:
        trig = add({"type": "trigger", "name": "intervaltime", "op1": "", "op2": "0", "op1type": "pay",
                    "op2type": "str", "duration": str(-abs(heartbeat)), "extend": False, "overrideDelay": False,
                    "units": "min", "reset": "", "bytopic": "all", "topic": "topic", "outputs": 1,
                    "wires": [[back["id"]]]}, 800, Y4)
        prep["wires"] = [[trig["id"]]]
    fmt = add(change("format msg.payload", [
        {"t": "set", "p": "payload.uuid", "pt": "msg", "to": ovar, "tot": "flow", "dc": True},
        {"t": "set", "p": "payload.isDelta", "pt": "msg", "to": "true", "tot": "bool"}], [[prep["id"]]]), 340, Y4)
    li_fmt["wires"] = [[fmt["id"]]]
    li_fmt["x"], li_fmt["y"] = 110, Y4
    pub = [li_fmt, fmt, prep, back, enc, mqout, enc_dbg]
    if heartbeat:
        pub.append(trig)
    group("prepare, encode and publish", pub)

    # ------------------------------------------------------------ error logging
    Y5 = Y4 + 130
    err_dbg = add(debug("error", active=True, complete="payload"), 800, Y5)
    err_tpl = add({"type": "template", "name": "create error message", "field": "payload", "fieldType": "msg",
                   "format": "handlebars", "syntax": "mustache", "output": "str",
                   "template": "[error] flow_id: {{flow_id}}, flow_name: {{flow_name}}, node_id: {{error.source.id}}, "
                               "node_name: {{error.source.name}},  {{error.message}}",
                   "wires": [[err_dbg["id"]]]}, 580, Y5)
    err_env = add(change("get env variables of flow", [
        {"t": "set", "p": "flow_id", "pt": "msg", "to": "$env('NR_FLOW_ID')", "tot": "jsonata"},
        {"t": "set", "p": "flow_name", "pt": "msg", "to": "$env('NR_FLOW_NAME')", "tot": "jsonata"}],
        [[err_tpl["id"]]]), 350, Y5)
    err_catch = add({"type": "catch", "name": "", "scope": None, "uncaught": False, "wires": [[err_env["id"]]]}, 130, Y5)
    group("error logging", [err_catch, err_env, err_tpl, err_dbg])

    tab = {"id": TAB, "type": "tab", "label": spec["tabLabel"], "disabled": False,
           "info": (spec.get("description", "") + "\n\nGenerated with ops-rule-engine "
                    f"(evaluate={evaluate}, output={out['name']} -> {out['field']}).").strip()}
    cfgnodes = [
        {"id": proto_id, "type": "protobuf-file", "protopath": "/data/plcschema.proto", "watchFile": True,
         "keepCase": False},
        {"id": broker_id, "type": "mqtt-broker", "name": "", "broker": "emqx.mqtt.svc", "port": "1883",
         "clientid": "", "autoConnect": True, "usetls": False, "protocolVersion": "4", "keepalive": "60",
         "cleansession": True, "birthTopic": "", "birthQos": "0", "birthPayload": "", "birthMsg": {},
         "closeTopic": "", "closeQos": "0", "closePayload": "", "closeMsg": {}, "willTopic": "", "willQos": "0",
         "willPayload": "", "willMsg": {}, "userProps": "", "sessionExpiry": ""}]
    flow = [tab] + groups + nodes + cfgnodes

    # sanity: every wire / link points at an existing node
    ids = {n["id"] for n in flow}
    for n in nodes:
        for o in n.get("wires", []):
            for tgt in o:
                assert tgt in ids, f"dangling wire from {n.get('name')}"
        for tgt in n.get("links", []):
            assert tgt in ids, f"dangling link from {n.get('name')}"
    return flow, out_topic


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    spec = json.load(open(sys.argv[1]))
    flow, out_topic = build(spec)
    json.dump(flow, open(sys.argv[2], "w"), indent=2, ensure_ascii=False)
    print(f"OK: {len(flow)} nodes -> {sys.argv[2]}")
    print(f"   in : {spec['inputTopic']}")
    print(f"   out: {out_topic}" + ("" if spec.get("outputTopic") else "   (derived from input topic - confirm with user)"))
