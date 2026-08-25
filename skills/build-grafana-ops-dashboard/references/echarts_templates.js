// =============================================================================
// echarts_templates.js — getOption JS for the bilibala-echarts-panel plugin
//
// Each template assumes the SQL target uses format=table and returns specific
// named columns. Templates read columns by NAME (not by position or type) which
// makes them robust to data shape variations.
//
// Every template includes two defensive splash screens:
//   - "No data" when the result set is empty
//   - "Unexpected data shape" when expected columns are missing
//
// These templates work identically for relational and timeseries archetypes —
// what matters is the column names the SQL produces.
//
// CONTENTS:
//   1. PARETO              — stacked bars + cumulative %
//   2. DONUT               — share by category
//   3. HEATMAP_DOW_HOUR    — day-of-week × hour-of-day intensity
//   4. COMPARE_BARS        — this-period vs prior-period horizontal bars
//   5. DURATION_HISTOGRAM  — bucketed bar chart with cumulative line
//   6. GAUGE               — single value with red/yellow/green zones
//   7. STATE_TIMELINE      — Gantt-like state strip (running/idle/fault)
//   8. HOURLY_OUTPUT       — bar (actual) + line (cumulative) + target line
//   9. SCATTER_WITH_LIMITS — scatter with UCL/LCL/target reference lines
//  10. KPI_CARD_GRID       — multiple KPIs in a single panel
//  11. CORRELATION_LINES   — two signals on dual y-axes
//  12. STACKED_AREA        — multi-series area chart for breakdown trends
// =============================================================================


// 1. PARETO ------------------------------------------------------------------
// SQL: format=table, columns:  metric (text "Group :: Item"), value (number)
const ECHARTS_PARETO_JS = `
const SEP = ' :: ';
const frame = data.series[0];
if (!frame || !frame.fields || frame.fields.length === 0) {
  return { title: { text: 'No data', left:'center', top:'center', textStyle:{color:'#888'} } };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;

const metricField = frame.fields.find(f => f.name === 'metric')
                 || frame.fields.find(f => f.type === 'string');
const valueField  = frame.fields.find(f => f.name === 'value')
                 || frame.fields.find(f => f.type === 'number');
if (!metricField || !valueField) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const metricVals = readVals(metricField);
const valueVals  = readVals(valueField);

const groupSet = new Set();
const itemSet  = new Set();
const cell = {};
for (let i = 0; i < metricVals.length; i++) {
  const label = String(metricVals[i] || '');
  const v = Number(valueVals[i]);
  if (!label || !isFinite(v) || v <= 0) continue;
  const parts = label.split(SEP);
  if (parts.length < 2) continue;
  const group = parts[0];
  const item  = parts.slice(1).join(SEP);
  groupSet.add(group); itemSet.add(item);
  cell[item] = cell[item] || {};
  cell[item][group] = (cell[item][group] || 0) + v;
}
if (itemSet.size === 0) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}

const groups = [...groupSet].sort();
const itemTotals = [...itemSet].map(r => ({
  item: r,
  total: groups.reduce((s, g) => s + (cell[r]?.[g] || 0), 0),
}));
itemTotals.sort((a,b) => b.total - a.total);
const categories = itemTotals.map(r => r.item);
const grandTotal = itemTotals.reduce((s,r) => s + r.total, 0);

const palette = ['#5470c6','#91cc75','#fac858','#ee6666','#73c0de',
                 '#3ba272','#fc8452','#9a60b4','#ea7ccc','#26a69a'];

const barSeries = groups.map((g, idx) => ({
  name: g, type: 'bar', stack: 'total',
  barMaxWidth: 36, barCategoryGap: '50%',
  itemStyle: { color: palette[idx % palette.length] },
  data: categories.map(r => Math.round((cell[r]?.[g] || 0) * 10) / 10),
}));

let running = 0;
const cumPct = itemTotals.map(r => {
  running += r.total;
  return Math.round((running / grandTotal) * 1000) / 10;
});

return {
  backgroundColor: 'transparent',
  tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
  legend: { top: 8, textStyle: { color: '#ccc' }, type: 'scroll' },
  grid: { left: 60, right: 60, top: 50, bottom: 20, containLabel: true },
  xAxis: { type:'category', data: categories,
           axisLabel: { color:'#ccc', rotate: 35, interval: 0,
                        formatter: v => v.length > 24 ? v.slice(0,22) + '\\u2026' : v } },
  yAxis: [
    { type:'value', name:'Value', nameTextStyle:{color:'#ccc'}, axisLabel:{color:'#ccc'} },
    { type:'value', name:'Cum %', min:0, max:100,
      nameTextStyle:{color:'#ccc'}, axisLabel:{color:'#ccc', formatter:'{value}%'} },
  ],
  series: [
    ...barSeries,
    { name:'Cumulative %', type:'line', yAxisIndex:1, data:cumPct,
      symbol:'circle', symbolSize:8, lineStyle:{width:3, color:'#f39c12'},
      itemStyle:{color:'#f39c12'},
      markLine:{ silent:true, symbol:'none', data:[{yAxis:80}],
                 lineStyle:{color:'#888', type:'dashed'} } },
  ],
};
`;


// 2. DONUT -------------------------------------------------------------------
// SQL: format=table, columns: <name_col>, <value_col>
const ECHARTS_DONUT_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });
const names = (cols['machine'] || cols['name'] || cols['category'] || cols['metric'] || []).map(String);
const vals  = (cols['hours'] || cols['value'] || cols['minutes'] || cols['count'] || []).map(Number);
if (names.length === 0) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}
const dataArr = names.map((n,i) => ({ name: n, value: vals[i] || 0 }));
const total = dataArr.reduce((s,d) => s + d.value, 0);

return {
  backgroundColor: 'transparent',
  tooltip: { trigger:'item', formatter: p => \`\${p.name}<br/><b>\${p.value}</b> (\${p.percent}%)\` },
  legend: { type:'scroll', orient:'vertical', right:10, top:'middle',
            textStyle:{color:'#ccc', fontSize:11} },
  title: { text: total.toFixed(1), subtext: 'total',
           left: '32%', top: '42%', textAlign:'center',
           textStyle:{color:'#ddd', fontSize:18, fontWeight:600},
           subtextStyle:{color:'#888', fontSize:11} },
  series: [{
    name:'Total', type:'pie',
    radius:['55%','80%'], center:['32%','50%'],
    avoidLabelOverlap:true, label:{show:false}, labelLine:{show:false},
    data: dataArr,
  }],
};
`;


// 3. HEATMAP_DOW_HOUR --------------------------------------------------------
// SQL: format=table, columns: day_of_week (0-6), hour_of_day (0-23), incidents
const ECHARTS_HEATMAP_DOW_HOUR_JS = `
const dows = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const hours = Array.from({length:24}, (_,i) => String(i).padStart(2,'0'));

const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });
const dowArr = cols['day_of_week'] || [];
const hourArr = cols['hour_of_day'] || [];
const incArr = cols['incidents'] || cols['count'] || cols['value'] || [];
if (!dowArr.length || !hourArr.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const cells = [];
let maxV = 0;
for (let i = 0; i < dowArr.length; i++) {
  const v = Number(incArr[i]) || 0;
  cells.push([Number(hourArr[i]), Number(dowArr[i]), v]);
  if (v > maxV) maxV = v;
}

return {
  backgroundColor: 'transparent',
  tooltip: { position:'top',
             formatter: p => \`\${dows[p.value[1]]} \${hours[p.value[0]]}:00<br/><b>\${p.value[2]}</b>\` },
  grid: { left: 60, right: 30, top: 30, bottom: 50, containLabel: true },
  xAxis: { type:'category', data: hours, splitArea:{show:true}, axisLabel:{color:'#ccc'} },
  yAxis: { type:'category', data: dows,  splitArea:{show:true}, axisLabel:{color:'#ccc'} },
  visualMap: { min:0, max:Math.max(1, maxV), calculable:true,
               orient:'horizontal', left:'center', bottom:5,
               textStyle:{color:'#ccc'},
               inRange:{color:['#0d2b45','#3a6ea5','#73c2fb','#fbf2c4','#f4845f','#d62828']} },
  series: [{
    type:'heatmap', data: cells,
    label:{show:true, color:'#000', fontSize:10},
    emphasis:{itemStyle:{shadowBlur:8, shadowColor:'rgba(0,0,0,0.5)'}},
  }],
};
`;


// 4. COMPARE_BARS ------------------------------------------------------------
// SQL: format=table, columns: <category_col>, this_week, prev_week
const ECHARTS_COMPARE_BARS_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });
const cats = (cols['machine'] || cols['category'] || cols['name'] || []).map(String);
const tw   = (cols['this_week'] || cols['current']  || []).map(Number);
const pw   = (cols['prev_week'] || cols['previous'] || []).map(Number);
if (!cats.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'axis', axisPointer:{type:'shadow'},
    formatter: ps => {
      const i = ps[0].dataIndex;
      const a = tw[i] || 0, b = pw[i] || 0;
      const delta = a - b;
      const pct = b > 0 ? ((delta/b)*100).toFixed(0) : '—';
      const arrow = delta > 0 ? '\\ud83d\\udd3a' : delta < 0 ? '\\ud83d\\udd3b' : '\\u25fc';
      return \`<b>\${cats[i]}</b><br/>This: <b>\${a}</b><br/>Prev: <b>\${b}</b><br/>\${arrow} \${delta>0?'+':''}\${delta.toFixed(1)} (\${pct}%)\`;
    } },
  legend:{ top:0, right:10, textStyle:{color:'#ccc'} },
  grid:{ left:80, right:30, top:30, bottom:30, containLabel:true },
  xAxis:{ type:'value', axisLabel:{color:'#ccc'},
          splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
  yAxis:{ type:'category', data: cats, inverse:true,
          axisLabel:{color:'#ccc',
                     formatter: v => v.length > 18 ? v.slice(0,16)+'\\u2026' : v} },
  series:[
    { name:'Previous', type:'bar', data:pw, itemStyle:{color:'#5c6b7d'},
      label:{show:true, position:'right', color:'#888', fontSize:10} },
    { name:'Current',  type:'bar', data:tw, itemStyle:{color:'#ee6666'},
      label:{show:true, position:'right', color:'#ddd', fontSize:11, fontWeight:600} },
  ],
};
`;


// 5. DURATION_HISTOGRAM ------------------------------------------------------
// SQL: format=table, columns: bucket (text), incidents (number), total_min (number)
const ECHARTS_DURATION_HISTOGRAM_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });
const buckets = (cols['bucket'] || []).map(String);
const incidents = (cols['incidents'] || cols['count'] || []).map(Number);
const totals = (cols['total_min'] || cols['total'] || []).map(Number);
if (!buckets.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'axis', axisPointer:{type:'shadow'} },
  grid:{ left:60, right:30, top:20, bottom:40, containLabel:true },
  xAxis:{ type:'category', data: buckets, axisLabel:{color:'#ccc'} },
  yAxis:[
    { type:'value', name:'Count', nameTextStyle:{color:'#ccc'},
      axisLabel:{color:'#ccc'},
      splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
    { type:'value', name:'Total', nameTextStyle:{color:'#ccc'},
      axisLabel:{color:'#ccc'}, splitLine:{show:false} },
  ],
  series:[
    { name:'Count', type:'bar', data:incidents, itemStyle:{color:'#5470c6'},
      label:{show:true, position:'top', color:'#ddd', fontSize:10} },
    { name:'Total', type:'line', yAxisIndex:1, data:totals,
      symbol:'circle', symbolSize:6,
      lineStyle:{color:'#f39c12', width:2}, itemStyle:{color:'#f39c12'} },
  ],
};
`;


// 6. GAUGE -------------------------------------------------------------------
// SQL: format=table, single row, column 'value' (number).
//      Optional columns: 'min', 'max' override the defaults.
// Edit GAUGE_TITLE / GAUGE_UNIT / ZONE_RED / ZONE_YELLOW for the metric.
const ECHARTS_GAUGE_JS = `
const GAUGE_TITLE  = 'Value';
const GAUGE_UNIT   = '';
const GAUGE_MIN    = 0;
const GAUGE_MAX    = 100;
const ZONE_RED     = 0.30;
const ZONE_YELLOW  = 0.70;

const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });
const valArr = cols['value'] || [];
if (!valArr.length) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}

const v = Number(valArr[valArr.length - 1]) || 0;
const min = (cols['min'] && cols['min'].length) ? Number(cols['min'][0]) : GAUGE_MIN;
const max = (cols['max'] && cols['max'].length) ? Number(cols['max'][0]) : GAUGE_MAX;

return {
  backgroundColor:'transparent',
  series: [{
    type:'gauge', min: min, max: max, radius:'90%',
    axisLine: { lineStyle: { width: 18,
        color: [[ZONE_RED,'#d62728'],[ZONE_YELLOW,'#f1a208'],[1,'#2ca02c']] } },
    pointer: { length:'60%', width:6, itemStyle:{color:'#ddd'} },
    axisTick:  { distance:-18, length:6,  lineStyle:{color:'#fff', width:1} },
    splitLine: { distance:-22, length:14, lineStyle:{color:'#fff', width:2} },
    axisLabel: { color:'#ccc', distance:-40, fontSize:11 },
    title:     { offsetCenter:[0, '-20%'], color:'#ccc', fontSize:13 },
    detail: { offsetCenter:[0, '0%'],
              formatter: '{value}' + GAUGE_UNIT,
              color:'#fff', fontSize:24, fontWeight:600 },
    data: [{ value: Math.round(v * 10) / 10, name: GAUGE_TITLE }],
  }],
};
`;


// 7. STATE_TIMELINE ----------------------------------------------------------
// SQL: format=table, columns: start_time, end_time, state (text), entity (optional)
const ECHARTS_STATE_TIMELINE_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const startVals = cols['start_time'] || cols['start'] || [];
const endVals   = cols['end_time']   || cols['end']   || [];
const stateVals = cols['state']      || cols['status'] || [];
const entityVals = cols['entity']    || cols['machine'] || cols['name'] || null;

if (!startVals.length || !stateVals.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const STATE_COLORS = {
  'running':       '#2ca02c',  'automatic':    '#2ca02c',
  'idle':          '#bbbbbb',  'standby':      '#bbbbbb',
  'manual':        '#3a6ea5',  'setup':        '#9a60b4',
  'stopped':       '#666666',
  'fault':         '#d62728',  'alarm':        '#d62728',
  'maintenance':   '#fac858',
};
const colorFor = (s) => STATE_COLORS[String(s).toLowerCase()] || '#888';

const entities = entityVals
  ? Array.from(new Set(entityVals.map(String)))
  : ['state'];

const seriesData = [];
for (let i = 0; i < startVals.length; i++) {
  const s = new Date(startVals[i]).getTime();
  const e = new Date(endVals[i] || startVals[i]).getTime();
  if (!isFinite(s) || !isFinite(e)) continue;
  const ent = entityVals ? String(entityVals[i]) : 'state';
  const yIdx = entities.indexOf(ent);
  const state = String(stateVals[i]);
  seriesData.push({
    name: state, value: [yIdx, s, e, state],
    itemStyle: { color: colorFor(state) },
  });
}

return {
  backgroundColor:'transparent',
  tooltip: {
    formatter: (p) => {
      const v = p.value;
      const s = new Date(v[1]).toLocaleString();
      const e = new Date(v[2]).toLocaleString();
      const dur = Math.round((v[2] - v[1]) / 60000);
      return \`<b>\${v[3]}</b><br/>\${entities[v[0]]}<br/>\${s} → \${e}<br/>\${dur} min\`;
    }
  },
  grid: { left: 100, right: 30, top: 20, bottom: 40, containLabel: true },
  xAxis: { type:'time', axisLabel:{color:'#ccc'} },
  yAxis: { type:'category', data: entities, inverse:true,
           axisLabel:{color:'#ccc',
                      formatter: v => v.length > 14 ? v.slice(0,12)+'\\u2026' : v} },
  series: [{
    type: 'custom',
    renderItem: (params, api) => {
      const yIdx = api.value(0);
      const x0 = api.coord([api.value(1), yIdx])[0];
      const x1 = api.coord([api.value(2), yIdx])[0];
      const y  = api.coord([api.value(1), yIdx])[1];
      const h  = api.size([0, 1])[1] * 0.7;
      return { type: 'rect',
               shape: { x: x0, y: y - h/2, width: Math.max(1, x1 - x0), height: h },
               style: api.style() };
    },
    encode: { x: [1, 2], y: 0 },
    data: seriesData,
  }],
};
`;


// 8. HOURLY_OUTPUT -----------------------------------------------------------
// SQL: format=table, columns: time (or hour_label), actual,
//                              cumulative (optional), target (optional)
const ECHARTS_HOURLY_OUTPUT_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const labelArr = cols['hour_label']
  || (cols['time'] ? cols['time'].map(t => {
       const d = new Date(t);
       return isNaN(d) ? String(t) : d.toLocaleString([], {hour:'2-digit', minute:'2-digit'});
     }) : []);
const actualArr     = (cols['actual']     || cols['ok']  || []).map(Number);
const cumulativeArr = (cols['cumulative'] || cols['cum'] || []).map(Number);
const targetArr     = (cols['target']     || []).map(Number);

if (!labelArr.length || !actualArr.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const series = [
  { name:'Actual', type:'bar', barWidth:'60%',
    data: actualArr,
    itemStyle: {
      color: (p) => {
        const t = targetArr[p.dataIndex];
        if (!t) return '#4CAF50';
        if (p.value >= t)         return '#4CAF50';
        if (p.value >= t * 0.9)   return '#FF9800';
        return '#F44336';
      }
    },
    label:{show:true, position:'inside', color:'#fff', fontSize:10},
  },
];

if (targetArr.length) {
  series.push({
    name:'Target', type:'line', data: targetArr,
    lineStyle:{color:'#FFC107', width:2, type:'dashed'},
    itemStyle:{color:'#FFC107'}, symbol:'circle', symbolSize:6,
  });
}

if (cumulativeArr.length) {
  series.push({
    name:'Cumulative', type:'line', yAxisIndex:1, smooth:true,
    data: cumulativeArr,
    lineStyle:{color:'#2196F3', width:2}, itemStyle:{color:'#2196F3'},
  });
}

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'axis', axisPointer:{type:'shadow'} },
  legend:{ top:0, textStyle:{color:'#ccc'} },
  grid:{ left:50, right:60, top:30, bottom:50, containLabel:true },
  xAxis:{ type:'category', data: labelArr,
          axisLabel:{color:'#ccc', rotate:45, fontSize:10} },
  yAxis:[
    { type:'value', name:'Per hour', axisLabel:{color:'#ccc'},
      splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
    { type:'value', name:'Cumulative', position:'right',
      axisLabel:{color:'#ccc'}, splitLine:{show:false} },
  ],
  series: series,
};
`;


// 9. SCATTER_WITH_LIMITS -----------------------------------------------------
// SQL: format=table, columns: time, value,
//                              ucl (optional), lcl (optional), target (optional)
const ECHARTS_SCATTER_LIMITS_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const timeArr = (cols['time'] || []).map(t => new Date(t).getTime());
const valArr  = (cols['value']  || []).map(Number);
const ucl = (cols['ucl'] && cols['ucl'].length)
              ? Number(cols['ucl'][cols['ucl'].length-1]) : null;
const lcl = (cols['lcl'] && cols['lcl'].length)
              ? Number(cols['lcl'][cols['lcl'].length-1]) : null;
const target = (cols['target'] && cols['target'].length)
              ? Number(cols['target'][cols['target'].length-1]) : null;

if (!timeArr.length || !valArr.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const points = timeArr.map((t,i) => {
  const v = valArr[i];
  const violation = (ucl !== null && v > ucl) || (lcl !== null && v < lcl);
  return { value: [t, v], itemStyle: { color: violation ? '#d62728' : '#3a6ea5' } };
});

const markLines = [];
if (ucl !== null)    markLines.push({ yAxis: ucl,    name:'UCL',    lineStyle:{color:'#d62728', type:'dashed'} });
if (lcl !== null)    markLines.push({ yAxis: lcl,    name:'LCL',    lineStyle:{color:'#d62728', type:'dashed'} });
if (target !== null) markLines.push({ yAxis: target, name:'Target', lineStyle:{color:'#2ca02c', type:'solid'} });

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'item',
    formatter: p => \`\${new Date(p.value[0]).toLocaleString()}<br/><b>\${p.value[1]}</b>\` },
  grid:{ left:50, right:30, top:30, bottom:40, containLabel:true },
  xAxis:{ type:'time', axisLabel:{color:'#ccc'} },
  yAxis:{ type:'value', axisLabel:{color:'#ccc'},
          splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
  series:[{
    type:'scatter', symbolSize:6, data: points,
    markLine: markLines.length ? {
      silent:true, symbol:'none',
      label:{position:'end', color:'#ccc', fontSize:10},
      data: markLines,
    } : undefined,
  }],
};
`;


// 10. KPI_CARD_GRID ----------------------------------------------------------
// SQL: format=table, columns: label (text), value (number),
//                              unit (text, optional),
//                              status (text: 'ok'|'warn'|'critical', optional)
const ECHARTS_KPI_GRID_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const labels = (cols['label'] || cols['name']  || []).map(String);
const values = (cols['value'] || cols['count'] || []).map(Number);
const units  = (cols['unit']  || []).map(String);
const status = (cols['status']|| []).map(String);

if (!labels.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const STATUS_COLORS = { ok:'#2ca02c', warn:'#fac858', critical:'#d62728' };

const n = labels.length;
const cols_ = Math.ceil(Math.sqrt(n));
const rows  = Math.ceil(n / cols_);

const graphics = labels.map((lbl, i) => {
  const row = Math.floor(i / cols_);
  const col = i % cols_;
  const xPct = ((col + 0.5) / cols_) * 100;
  const yPct = ((row + 0.5) / rows ) * 100;
  const color = STATUS_COLORS[(status[i] || 'ok').toLowerCase()] || '#ddd';
  const valText = String(values[i]) + (units[i] ? ' ' + units[i] : '');
  return [
    { type:'text', left: xPct + '%', top: (yPct - 8) + '%', z: 100,
      style:{ text: valText, fill: color, fontSize: 28, fontWeight: 700,
              textAlign: 'center', textVerticalAlign: 'middle' } },
    { type:'text', left: xPct + '%', top: (yPct + 4) + '%', z: 100,
      style:{ text: lbl, fill: '#aaa', fontSize: 12,
              textAlign: 'center', textVerticalAlign: 'middle' } },
  ];
}).flat();

return {
  backgroundColor: 'transparent',
  graphic: graphics,
};
`;


// 11. CORRELATION_LINES ------------------------------------------------------
// SQL: format=table, columns: time, <signal_a>, <signal_b>
// Picks the two numeric (non-time) columns; aliases set the legend names.
const ECHARTS_CORRELATION_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const timeArr = (cols['time'] || []).map(t => new Date(t).getTime());

const numericFields = frame.fields.filter(f =>
  f.type === 'number' && f.name.toLowerCase() !== 'time'
);
if (numericFields.length < 2) {
  return { title:{text:'Need 2 numeric series', left:'center', top:'center', textStyle:{color:'#c66'}} };
}
const aName = numericFields[0].name;
const bName = numericFields[1].name;
const aArr = readVals(numericFields[0]).map(Number);
const bArr = readVals(numericFields[1]).map(Number);

const aData = timeArr.map((t,i) => [t, aArr[i]]);
const bData = timeArr.map((t,i) => [t, bArr[i]]);

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'axis' },
  legend:{ top:0, textStyle:{color:'#ccc'} },
  grid:{ left:50, right:60, top:30, bottom:40, containLabel:true },
  xAxis:{ type:'time', axisLabel:{color:'#ccc'} },
  yAxis:[
    { type:'value', name: aName, position:'left',
      nameTextStyle:{color:'#5470c6'}, axisLabel:{color:'#ccc'},
      splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
    { type:'value', name: bName, position:'right',
      nameTextStyle:{color:'#ee6666'}, axisLabel:{color:'#ccc'},
      splitLine:{show:false} },
  ],
  series:[
    { name:aName, type:'line', data:aData,
      yAxisIndex:0, lineStyle:{color:'#5470c6', width:2}, symbol:'none', smooth:true },
    { name:bName, type:'line', data:bData,
      yAxisIndex:1, lineStyle:{color:'#ee6666', width:2}, symbol:'none', smooth:true },
  ],
};
`;


// 12. STACKED_AREA -----------------------------------------------------------
// SQL: format=table, columns: time, metric (text), value (number)
const ECHARTS_STACKED_AREA_JS = `
const frame = data.series[0];
if (!frame || !frame.fields) {
  return { title:{text:'No data', left:'center', top:'center', textStyle:{color:'#888'}} };
}
const readVals = (f) => typeof f.values.toArray === 'function' ? f.values.toArray() : f.values;
const cols = {};
frame.fields.forEach(f => { cols[f.name] = readVals(f); });

const timeArr   = (cols['time']   || []).map(t => new Date(t).getTime());
const metricArr = (cols['metric'] || []).map(String);
const valueArr  = (cols['value']  || []).map(Number);

if (!timeArr.length || !metricArr.length) {
  return { title:{text:'Unexpected data shape', left:'center', top:'center', textStyle:{color:'#c66'}} };
}

const byMetric = {};
const allTimes = new Set();
for (let i = 0; i < timeArr.length; i++) {
  const t = timeArr[i];
  const m = metricArr[i];
  const v = Number(valueArr[i]) || 0;
  byMetric[m] = byMetric[m] || {};
  byMetric[m][t] = (byMetric[m][t] || 0) + v;
  allTimes.add(t);
}
const times = [...allTimes].sort((a,b) => a - b);
const metrics = Object.keys(byMetric);

const palette = ['#5470c6','#91cc75','#fac858','#ee6666','#73c0de',
                 '#3ba272','#fc8452','#9a60b4','#ea7ccc','#26a69a'];

const series = metrics.map((m, idx) => ({
  name: m, type:'line', stack:'total', areaStyle: {opacity: 0.7},
  symbol:'none', smooth:false,
  itemStyle:{color: palette[idx % palette.length]},
  data: times.map(t => [t, byMetric[m][t] || 0]),
}));

return {
  backgroundColor:'transparent',
  tooltip:{ trigger:'axis' },
  legend:{ top:0, textStyle:{color:'#ccc'}, type:'scroll' },
  grid:{ left:50, right:30, top:30, bottom:40, containLabel:true },
  xAxis:{ type:'time', axisLabel:{color:'#ccc'} },
  yAxis:{ type:'value', axisLabel:{color:'#ccc'},
          splitLine:{lineStyle:{color:'rgba(255,255,255,0.08)'}} },
  series: series,
};
`;


// =============================================================================
// CHART-PICKING GUIDE
// =============================================================================
//
//   Ranking with 80/20 emphasis           → PARETO
//   Share of total                        → DONUT
//   When-do-things-cluster                → HEATMAP_DOW_HOUR
//   This-period vs prior                  → COMPARE_BARS
//   Distribution of a measurement         → DURATION_HISTOGRAM
//   Single-value KPI with thresholds      → GAUGE
//   Machine state over time (Gantt-like)  → STATE_TIMELINE
//   Production output vs target           → HOURLY_OUTPUT
//   SPC / quality with control limits     → SCATTER_WITH_LIMITS
//   Multiple KPIs in one panel            → KPI_CARD_GRID
//   Two signals together (correlation)    → CORRELATION_LINES
//   Breakdown trend (stacked over time)   → STACKED_AREA
//
// Defensive splash screens are NOT optional. If a panel renders blank, the
// splash should fire — if it doesn't, the splash got stripped or SQL silently
// returned no rows.
//
// For GAUGE: edit ZONE_RED / ZONE_YELLOW / GAUGE_UNIT at the top of the JS.
// For STATE_TIMELINE: extend STATE_COLORS for domain-specific state names.
