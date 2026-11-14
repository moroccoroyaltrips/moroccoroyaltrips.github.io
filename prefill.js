// Pre-render English text into the HTML so content shows before scripts run
const fs=require('fs');let n=0,tot=0;
for(const f of process.argv.slice(2)){
  let s=fs.readFileSync(f,'utf8');const i=s.indexOf('const T={');if(i<0)continue;
  const j=s.indexOf('\n};',i);const T=Function('return '+s.slice(i+8,j+2))();const en=T.en;
  const a=s.lastIndexOf('<script',i);const head=s.slice(0,a),tail=s.slice(a);
  let c=0;
  const out=head.replace(/(<([a-zA-Z0-9]+)\b[^>]*?\sdata-i="([^"]+)"[^>]*>)(x?)(<\/\2>)/g,(m,o,t,k,x,cl)=>{if(en[k]===undefined)return m;c++;return o+en[k]+cl});
  fs.writeFileSync(f,out+tail);n++;tot+=c;
}
console.log('prefilled',n,'files',tot,'elements');
