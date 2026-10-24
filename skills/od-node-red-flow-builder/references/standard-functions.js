/* Standard Node-RED function nodes — OESL shop-floor flows.
 *
 * Verbatim from the flow corpus (825 flows, 53 ct-oesl instances). Copy these rather
 * than rewriting: the sysTime pair in particular is easy to get subtly wrong, and a
 * wrong one corrupts every downstream timestamp silently.
 *
 * Counts are the number of flows in the corpus carrying a node of that exact name.
 */

// ─────────────────────────────────────────────────────────────────────────────
// "Convert sysTime (UTC timestamp)"  — 625 flows
//
// Inbound. PLCPacket.sys_time is a packed uint64: the upper four bytes are seconds
// since epoch, the lower four are nanoseconds. Unpack to epoch milliseconds (UTC).
// Sits directly after the split that flattens the plcPackets array.
// ─────────────────────────────────────────────────────────────────────────────
var sysTime = msg.payload.sysTime

const seconds_epoch = Number(BigInt(sysTime) >> 32n)   // first four bytes: seconds since 1.1.1970
const nanos         = Number(BigInt(sysTime) & 0xFFFFFFFFn)  // last four bytes: nanoseconds
const millis        = Math.round(nanos / 1e6)
const millis_epoch  = seconds_epoch * 1000 + millis    // UTC

msg.payload.sysTime = millis_epoch

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "Convert sysTime back (UTC timestamp)"  — 617 flows
//
// Outbound. Re-pack before the protobuf encode. Note this stamps *now*, not the
// inbound time: a derived signal is timestamped when it is derived. If you need to
// carry the source timestamp through instead, re-pack the value you unpacked — and
// say so in the node's info, because it departs from the house pattern.
// ─────────────────────────────────────────────────────────────────────────────
const dt_new = new Date()
const dt     = dt_new.getTime()

const in_left = Math.round(dt / 1000)
const nanos_p = BigInt(in_left) << 32n | BigInt(dt_new.getMilliseconds() * 1e6)

msg.payload.plcPackets[0].sysTime = Number(nanos_p)

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "filter uuids"  — 599 flows
//
// The gate. Keeps only the packets this flow cares about. The UUID list comes from
// flow config, never from a literal here. Add each additional data point to the array.
//
// Node info (kept in the corpus, worth keeping):
//   1. loop over msg.payload.plcPackets
//   2. skip if uuid (or other filters) does not match
//   3. emit entire plcPackets if uuid matches
// ─────────────────────────────────────────────────────────────────────────────
const uuids = [flow.get('datapointTotalPartCounter')]

const results = msg.payload.plcPackets.filter(plcPacket => uuids.includes(plcPacket.uuid))

msg.payload = results

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "Debug flow config"  — 675 flows
//
// Echoes what the config group actually set, so a mistyped UUID shows up at deploy
// time on the debug pane instead of as an empty dashboard a week later.
// Mirror the exact variables your "Set flow config" node writes.
// ─────────────────────────────────────────────────────────────────────────────
var payload = {
    datatronName:                 flow.get('datatronName'),
    datapointTotalPartCounter:    flow.get('datapointTotalPartCounter'),
    datapointPartProducedTrigger: flow.get('datapointPartProducedTrigger')
};

return {
    payload: payload,
    debugInfo: "Added flow configuration"
};


// ─────────────────────────────────────────────────────────────────────────────
// "set device endpoint"  — 41 flows
//
// Resolves the datatron's device id. Always runs before "set data_points endpoint"
// below — the two are one request chain, not two independent ones.
// ─────────────────────────────────────────────────────────────────────────────
var baseUrl    = msg.url
var datatronId = msg.payload.id
var postfixUrl = "/devices"

msg.url     = baseUrl + "/" + datatronId + postfixUrl
msg.headers = flow.get("headers")

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "set data_points endpoint"  — 41 flows
//
// Builds the IIoT edge platform query that resolves data points for a datatron, so
// UUIDs are fetched rather than typed. Preceded by a request that resolves the
// datatron id; headers (incl. the Bearer token) come from flow config, never a literal.
// ─────────────────────────────────────────────────────────────────────────────
var baseUrl    = msg.url
var datatronId = msg.payload.id
var postfixUrl = "/data_points"

msg.url     = baseUrl + "/" + datatronId + postfixUrl
msg.headers = flow.get("headers")

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "set datapointConfigFilter"  — 205 flows
//
// Defines which UUIDs "filter uuids" (above) keeps. One array, built from flow
// config, one entry per data point this flow consumes — never a literal UUID.
// ─────────────────────────────────────────────────────────────────────────────
const uuids = [flow.get('datapointCycleStart'), flow.get('datapointCycleEnd')]

flow.set("datapointConfigFilter", uuids);

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "calculate timerange between cycle_start and cycle_end event"  — 148 flows
//
// The P3 two-event time range (see transformation-patterns.md), under the name it
// actually carries in the corpus. Both guards are load-bearing — see there for why.
// ─────────────────────────────────────────────────────────────────────────────
var cycle_start_time = msg.payload.sysTimeStart;
var cycle_end_time   = msg.payload.sysTimeEnd;

msg.payload.cycle_time = ((cycle_end_time - cycle_start_time) / 1000)

if (isNaN(msg.payload.cycle_time)) { return null; }
if (msg.payload.cycle_time < 0)    { return null; }

return msg;


// ─────────────────────────────────────────────────────────────────────────────
// "create json payload"  — 157 flows
//
// The publish step that follows the calculation above: wraps a derived value into
// a PLCPacket-shaped object under its OWN output uuid, ready for "prepare for protob
// encoding". `sysTime` here is carried over from the triggering event, not re-stamped
// — that is a deliberate choice, unlike P8's "build from nothing", which has no event
// to carry a timestamp from and so packs `sysTime` itself.
// ─────────────────────────────────────────────────────────────────────────────
var uuid        = flow.get('datapointCycleTime')
var sysTime     = msg.payload.sysTimeEnd
var valueDouble = msg.payload.cycle_time

msg.payload = {
    uuid: uuid,
    sysTime: sysTime,
    valueDouble: valueDouble,
    isDelta: true
}

return msg;
