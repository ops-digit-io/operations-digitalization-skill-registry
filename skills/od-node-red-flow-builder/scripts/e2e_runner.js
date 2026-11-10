const {Aedes} = require('aedes'); const net=require('net'); const {spawn}=require('child_process');
const mqtt=require('mqtt'); const protobuf=require('protobufjs');
const [batchFile, inTopic, outTopic, outUuid] = process.argv.slice(2);
(async()=>{ const aedes = Aedes.createBroker ? await Aedes.createBroker() : new Aedes(); net.createServer(aedes.handle).listen(18830, async () => {
  const root = await protobuf.load('plcschema.proto'); const T = root.lookupType('PLCPacketList');
  const nr = spawn('node', ['node_modules/node-red/red.js','-u','ud','-p','18800'], {stdio:['ignore','pipe','pipe']});
  let log=''; nr.stdout.on('data',d=>log+=d); nr.stderr.on('data',d=>log+=d);
  await new Promise(r=>setTimeout(r,9000));
  const c = mqtt.connect('mqtt://127.0.0.1:18830');
  c.on('connect', async () => {
    c.subscribe(outTopic);
    c.on('message',(t,buf)=>{ try{ const m=T.toObject(T.decode(buf),{longs:String}); m.plcPackets.forEach(p=>{ if(p.uuid===outUuid){ const s=BigInt(p.sysTime)>>32n; console.log('OUT', JSON.stringify({...p, sysTimeISO:new Date(Number(s)*1000).toISOString()}));}});}catch(e){console.log('decode err',e.message)} });
    const batches = require(batchFile);
    for (const b of batches) {
      const now=BigInt(Math.floor(Date.now()/1000))<<32n;
      const msg=T.fromObject({plcPackets:b.map(p=>({sysTime:now.toString(),isDelta:true,...p}))});
      c.publish(inTopic, Buffer.from(T.encode(msg).finish())); console.log('IN ', JSON.stringify(b.map(p=>p.valueInteger)));
      await new Promise(r=>setTimeout(r,800));
    }
    await new Promise(r=>setTimeout(r,1500));
    console.log('--- node-red log (warnings/errors) ---'); console.log(log.split('\n').filter(l=>/warn|error|Started flows|Connected/i.test(l)).join('\n'));
    nr.kill(); process.exit(0);
  });
});
})();
