/* RiskAI v3.5.2 unambiguous probability and scale display */
(function(){
 const clamp01=x=>Math.min(1,Math.max(0,Number.isFinite(x)?x:0));
 const nnbsp='\u202f';
 function formatMicromort(value){
   const parts=Math.min(1e6,Math.max(0,value)).toFixed(4).split('.');
   const grouped=parts[0].replace(/\B(?=(\d{3})+(?!\d))/g,nnbsp);
   return grouped+','+parts[1];
 }
 function formatPercent(p){return (100*clamp01(p)).toLocaleString(lang==='de'?'de-DE':'en-US',{minimumFractionDigits:4,maximumFractionDigits:4})+' %'}
 function formatOdds(p){p=clamp01(p);return p<=0?'–':p>=1?'1 : 1':'1 : '+Math.round(1/p).toLocaleString(lang==='de'?'de-DE':'en-US')}
 function band(m){return m<.1?['Very low','Sehr niedrig','green']:m<1?['Low','Niedrig','blue']:m<10?['Medium','Mittel','yellow']:m<100?['High','Hoch','orange']:m<1000?['Very high','Sehr hoch','red']:m<10000?['Extreme','Extrem','red2']:m<100000?['Very extreme','Sehr extrem','red3']:m<900000?['Critical','Kritisch','red4']:['Near-certain in model','Nahezu sicher im Modell','black']}
 function position(m){return m>0?Math.min(100,Math.max(0,12.5*(Math.log10(Math.max(m,.01))+2))):0}
 function add(){
   const card=document.querySelector('.resultCard');
   if(!card||document.querySelector('#scaleMeaning'))return;
   card.insertAdjacentHTML('beforeend',`<details id="scaleMeaning" class="probabilityGuard"><summary>${lang==='de'?'Zahl und Skala richtig lesen':'How to read the number and scale'}</summary><p>${lang==='de'?'Schmale Leerzeichen trennen Tausender, das Komma trennt Dezimalstellen. Beispiel: 5 000,0000 µMort sind fünftausend µMort, nicht fünf Millionen. Das entspricht 0,5000 % beziehungsweise etwa 1 zu 200.':'Narrow spaces separate thousands and the decimal point separates decimals. Example: 5 000.0000 µMort is five thousand µMort, not five million. This equals 0.5000% or about 1 in 200.'}</p><p>${lang==='de'?'Die Skala reicht von 0,01 bis 1 000 000 µMort. 1 000 000 µMort entsprechen 100 %.':'The scale spans 0.01 to 1,000,000 µMort. 1,000,000 µMort equals 100%.'}</p><p id="rangeWarning"></p></details>`);
 }
 const prior=calculate;
 calculate=function(){
   prior();
   const H=results().filter(x=>x.m.model).reduce((sum,x)=>sum+Math.max(0,x.H||0),0);
   const P=clamp01(-Math.expm1(-H));
   const M=Math.min(1e6,1e6*P);
   const b=band(M);
   $('#mm').textContent=formatMicromort(M);
   $('#prob').textContent=formatPercent(P)+' · '+formatOdds(P);
   $('#band').textContent=b[lang==='de'?1:0];
   $('#band').className='pill '+b[2];
   $('#needle').style.left=position(M)+'%';
   $('#needle').setAttribute('aria-label',formatMicromort(M)+' µMort, '+formatPercent(P));
   const w=$('#rangeWarning'),km=acts.reduce((s,a)=>s+(Number(a.km)||0),0);
   if(w){w.className=km>2000?'modelWarning':'';w.textContent=km>2000?(lang==='de'?'Außerhalb eines plausiblen Tagesbereichs: mathematische Extrapolation.':'Outside a plausible daily range: mathematical extrapolation.'):''}
   window.current={...(window.current||{}),hazard:H,probability:P,micromort:M,probability_percent:100*P,odds:formatOdds(P)};
 };
 add(); calculate();
})();