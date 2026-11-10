#!/usr/bin/env bash
# e2e_test.sh - run a generated flow in a real, throw-away Node-RED + local MQTT broker.
#
# Usage: bash e2e_test.sh <flow.json> <batches.json> <output-uuid>
#
# Installs node-red, node-red-contrib-protobuf, aedes, mqtt into /tmp/ops-rule-e2e (once),
# rewrites broker -> 127.0.0.1:18830 and the proto path -> test_plcschema.proto,
# publishes each batch to the flow's input topic and prints every output packet.
# NOTE: test_plcschema.proto is a stand-in with the known PLCPacket field names;
# the production /data/plcschema.proto is authoritative.
set -euo pipefail
FLOW=$(realpath "$1"); BATCHES=$(realpath "$2"); OUTUUID="$3"
HERE=$(cd "$(dirname "$0")" && pwd)
W=/tmp/ops-rule-e2e
mkdir -p "$W/ud"
cd "$W"
if [ ! -d node_modules/node-red ]; then
  npm init -y >/dev/null
  npm install --silent node-red node-red-contrib-protobuf aedes mqtt protobufjs
fi
cp "$HERE/test_plcschema.proto" plcschema.proto
python3 - "$FLOW" "$W" <<'PY'
import json, sys
flow, w = sys.argv[1], sys.argv[2]
f = json.load(open(flow)); tin = tout = None
for n in f:
    if n['type'] == 'mqtt-broker': n['broker'] = '127.0.0.1'; n['port'] = '18830'
    if n['type'] == 'protobuf-file': n['protopath'] = w + '/plcschema.proto'
    if n['type'] == 'mqtt in': tin = n['topic']
    if n['type'] == 'mqtt out': tout = n['topic']
json.dump(f, open(w + '/ud/flows.json', 'w'))
open(w + '/topics', 'w').write(f"{tin.rstrip('#').rstrip('/').replace('/+','/x')}\n{tout}\n")
PY
TIN=$(sed -n 1p topics); TOUT=$(sed -n 2p topics)
cp "$HERE/e2e_runner.js" .
timeout 90 node e2e_runner.js "$BATCHES" "$TIN" "$TOUT" "$OUTUUID"
