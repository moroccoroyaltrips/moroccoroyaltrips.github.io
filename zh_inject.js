// add a zh dictionary to every page's T object, from the translation memory in zh_tm/*.json (keyed by English text)
const fs=require('fs'),vm=require('vm'),path=require('path');
const TM={};for(const f of fs.readdirSync('zh_tm').filter(f=>f.endsWith('.json')).sort())Object.assign(TM,JSON.parse(fs.readFileSync('zh_tm/'+f,'utf8')));
const MON={Jan:1,Feb:2,Mar:3,Apr:4,May:5,Jun:6,Jul:7,Aug:8,Sep:9,Oct:10,Nov:11,Dec:12};
function tr(v){if(typeof v!=='string')return v;if(TM[v]!==undefined)return TM[v];
 const m=v.match(/^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d+), (\d{4})$/);if(m)return m[3]+'年'+MON[m[1]]+'月'+m[2]+'日';
 miss.add(v);return v}
const miss=new Set();
function getT(s){const i=s.indexOf('const T={');if(i<0)return null;let d=0,j=i+8;for(;j<s.length;j++){const c=s[j];if(c==='"'||c==="'"||c==='`'){const q=c;j++;while(j<s.length&&s[j]!==q){if(s[j]==='\\')j++;j++}continue}if(c==='{')d++;else if(c==='}'){d--;if(d===0)break}}return {start:i+8,end:j+1,src:s.slice(i+8,j+1)}}
let n=0;
for(const f of process.argv.slice(2)){let s=fs.readFileSync(f,'utf8');const t=getT(s);if(!t)continue;
 const T=vm.runInNewContext('('+t.src+')');if(T.zh)continue;
 const zh={};for(const [k,v] of Object.entries(T.en))zh[k]=tr(v);
 const body=Object.entries(zh).map(([k,v])=>JSON.stringify(k)+':'+JSON.stringify(v)).join(',');
 s=s.slice(0,t.end-1)+',\n zh:{'+body+'}\n'+s.slice(t.end-1);fs.writeFileSync(f,s);n++}
// search index
if(fs.existsSync('search-index.js')){const ctx={window:{}};vm.runInNewContext(fs.readFileSync('search-index.js','utf8'),ctx);const idx=ctx.window.SRCH_IDX;
 for(const x of idx){if(x.t&&x.t.en)x.t.zh=tr(x.t.en);if(x.r&&x.r.en)x.r.zh=tr(x.r.en)}
 fs.writeFileSync('search-index.js','window.SRCH_IDX='+JSON.stringify(idx)+';')}
fs.writeFileSync('zh_missing.json',JSON.stringify([...miss],null,0));
console.log('zh injected',n,'pages; TM',Object.keys(TM).length,'missing',miss.size);
