(async()=>{
const $=s=>document.querySelector(s),W=320,H=180,cv=$('#game'),g=cv.getContext('2d');g.imageSmoothingEnabled=false;
const M=MANIFEST,CT=CONTENT,ST=STAGES,RM=matchMedia('(prefers-reduced-motion: reduce)').matches,rd=Math.round;
const IM={};await Promise.all(Object.keys(M).map(k=>new Promise(r=>{const i=new Image();i.onload=i.onerror=r;i.src=M[k].src;IM[k]=i})));
const S={i:0,mode:'title',found:{},q:[],cb:null,o:{},ty:null,tm:0,tm2:0,cur:'',shown:'',acc:'',pc:0,lk:0,kf:0,script:null,si:0,wait:false,end:false,done:false,fin:false,hop:{},parts:[],tr:null,fi:0,snd:true,wp:0,reveal:0,give:0,hx:60,hp:null};
const spr=(n,x,y,f=0,ch,al)=>{const m=M[n];if(al!=null)g.globalAlpha=al;g.drawImage(IM[n],f*m.w,0,m.w,ch||m.h,rd(x),rd(y+(m.dy||0)),m.w,ch||m.h);g.globalAlpha=1};
const rect=(c,x,y,w,h)=>{g.fillStyle=c;g.fillRect(rd(x),rd(y),w,h)};
// áudio 100% sintetizado (WebAudio): sons de máquina de escrever e trilha chiptune original
let AC=null,MG,SG,mt=0,stp=0,nx=0,NB;
function ac(){if(AC===false)return null;if(!AC){try{AC=new(window.AudioContext||window.webkitAudioContext)();MG=AC.createGain();MG.gain.value=.3;MG.connect(AC.destination);SG=AC.createGain();SG.connect(AC.destination)}catch(e){AC=false;return null}}if(AC.state=='suspended')AC.resume();return AC}
const mf=n=>440*Math.pow(2,(n-69)/12);
function tone(t,f,d,ty,v,dst,f2){const o=AC.createOscillator(),a=AC.createGain();if(typeof ty=='string')o.type=ty;else o.setPeriodicWave(ty);o.frequency.setValueAtTime(f,t);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t+d);a.gain.setValueAtTime(v,t);a.gain.exponentialRampToValueAtTime(.0001,t+d);o.connect(a);a.connect(dst);o.start(t);o.stop(t+d+.02)}
function noise(t,d,v,dst){if(!NB){NB=AC.createBuffer(1,AC.sampleRate*.3,AC.sampleRate);const c=NB.getChannelData(0);for(let i=0;i<c.length;i++)c[i]=Math.random()*2-1}const s=AC.createBufferSource(),a=AC.createGain();s.buffer=NB;a.gain.setValueAtTime(v,t);a.gain.exponentialRampToValueAtTime(.0001,t+d);s.connect(a);a.connect(dst);s.start(t);s.stop(t+d)}
function sfx(k,i=0){if(!S.snd||!ac())return;const t=AC.currentTime;
 if(k=='key'){noise(t,.03,.22,SG);tone(t,190+Math.random()*90,.05,'triangle',.16,SG,90)}
 else if(k=='space'){noise(t,.04,.25,SG);tone(t,110,.08,'triangle',.2,SG,60)}
 else if(k=='ding'){tone(t,1760,.55,'sine',.07,SG);tone(t,2640,.4,'sine',.03,SG)}
 else if(k=='btn')tone(t,440,.07,'square',.04,SG,660)
 else if(k=='select'){tone(t,660,.08,'square',.05,SG);tone(t+.07,880,.1,'square',.05,SG)}
 else if(k=='found'||k=='done')[523,659,784,1047].slice(0,k=='done'?4:3).forEach((f,j)=>tone(t+j*.09,f,.16,'square',.05,SG))
 else if(k=='whoosh')tone(t,900,.35,'triangle',.07,SG,150)
 else if(k=='note'){const n=[72,74,76,79,81,84][i%6];tone(t,mf(n),.4,'square',.06,SG);tone(t+.12,mf(n),.3,'square',.02,SG)}
 else if(k=='heart')[784,988,1175,1568].forEach((f,j)=>tone(t+j*.1,f,.3,'triangle',.06,SG))}
let ss=0;const NN={c:0,d:2,e:4,f:5,g:7,a:9,b:11};
const LEAD=("e5 - g5 - e5 d5 c5 - d5 - g5 - b4 - d5 - e5 - c5 e5 a5 - g5 e5 g5 - e5 - d5 - b4 - f5 - a5 - c6 - a5 f5 e5 - g5 e5 c5 - d5 e5 f5 - e5 d5 c5 - a4 - b4 - d5 g5 - - - - "+
 "a5 - c6 - b5 a5 g5 - a5 - f5 - c6 - a5 - g5 - e5 g5 c6 - b5 g5 d6 - b5 - g5 - d5 - c6 - e6 - d6 c6 b5 - c6 - a5 - f5 - a5 c6 d6 - b5 - g5 - b5 - c6 - - - e5 - c5 -").split(' ').map(k=>k=='-'?'-':12*(+k[1]+1)+NN[k[0]]);
const CHD={C:[48,[60,64,67]],G:[43,[59,62,67]],Am:[45,[57,60,64]],Em:[40,[59,64,67]],F:[41,[57,60,65]]},PRG='C G Am Em F C F G Am F C G F C G C'.split(' ');
let P25,P12;const pw=d=>{const n=24,re=new Float32Array(n),im=new Float32Array(n);for(let k=1;k<n;k++){re[k]=2/(k*Math.PI)*Math.sin(k*Math.PI*d);im[k]=2/(k*Math.PI)*(1-Math.cos(k*Math.PI*d))}return AC.createPeriodicWave(re,im)};
function lead(t,f,d){const o=AC.createOscillator(),a=AC.createGain(),l=AC.createOscillator(),lg=AC.createGain();o.setPeriodicWave(P25);o.frequency.value=f;l.frequency.value=5.2;lg.gain.value=d>.5?7:0;l.connect(lg);lg.connect(o.detune);
 a.gain.setValueAtTime(.0001,t);a.gain.linearRampToValueAtTime(.05,t+.03);a.gain.setValueAtTime(.045,t+d*.7);a.gain.exponentialRampToValueAtTime(.0001,t+d);o.connect(a);a.connect(MG);o.start(t);l.start(t);o.stop(t+d+.02);l.stop(t+d+.02)}
const E8=60/92/2;
function sched(){while(nx<AC.currentTime+.3){const s=ss%128,b=s>>3,st=s&7,[bs,tr]=CHD[PRG[b]],t=nx,n=LEAD[s];
 if(st==0||st==4)tone(t,mf(bs+(st==4&&PRG[b]!='Em'?7:0)),E8*3.6,'triangle',.2,MG);
 tone(t,mf(tr[[0,1,2,1,0,1,2,1][st]]+12),E8*1.2,P12,.02,MG);
 if(typeof n=='number'){let l=1;while(LEAD[(s+l)%128]=='-'&&l<8)l++;lead(t,mf(n),E8*l*.94);tone(t+E8*.75,mf(n),E8*1.5,P12,.012,MG)}
 if(st==0)tone(t,120,.14,'sine',.2,MG,45);if(st%2==1)noise(t,.02,.012,MG);ss++;nx+=E8}}
function music(on){clearInterval(mt);if(on&&ac()){P25=pw(.25);P12=pw(.125);nx=AC.currentTime+.1;ss=0;mt=setInterval(sched,50)}}
$('#mus').onclick=()=>{S.snd=!S.snd;$('#mus').textContent=S.snd?'♪':'✕';music(S.snd)};$('#vol').oninput=ev=>{if(MG)MG.gain.value=+ev.target.value*.6};
addEventListener('click',ev=>{if(ev.target&&ev.target.tagName=='BUTTON')sfx('btn')});
addEventListener('keydown',ev=>{if(S.mode=='play'&&!ev.repeat)sfx(ev.key==' '?'space':'key')});
// diálogo (texto digitado)
const fc=$('#face').getContext('2d');fc.imageSmoothingEnabled=false;
function drawFace(){const s=ST[S.i],n='face_'+(s.face||'e'),m=M[n];fc.clearRect(0,0,40,42);fc.drawImage(IM[n],(S.fi%5)*m.w,0,m.w,m.h,0,0,40,42)}
const tx=$('#tx'),dlg=$('#dlg'),busy=()=>!!S.ty||S.q.length>0;
function paint(){tx.textContent=(S.o.letter?S.acc:'')+S.shown;dlg.classList.toggle('letter',!!S.o.letter);dlg.scrollTop=dlg.scrollHeight;
 dlg.classList.toggle('wait',!S.ty&&(S.q.length>0||(!!S.script&&!S.wait&&!S.end)));$('#skip').hidden=!(S.o.keys&&(S.ty||S.q.length))}
function say(lines,cb,o={}){clearTimeout(S.tm);clearInterval(S.ty);S.ty=null;S.q=[...lines];S.cb=cb||null;S.o=o;S.acc='';S.shown='';adv()}
function adv(){if(S.ty){endLine();return}if(S.q.length)line(S.q.shift())}
function line(t){S.cur=t;let k=0;S.shown='';paint();S.ty=setInterval(()=>{k++;S.shown=t.slice(0,k);if(S.o.keys){sfx(t[k-1]==' '?'space':'key');if(t[k-1]!=' '){S.lk=performance.now();S.kf=1+Math.floor(Math.random()*5);S.pc++}}paint();if(k>=t.length)endLine()},S.o.keys?55:24)}
function endLine(){clearInterval(S.ty);S.ty=null;S.shown=S.cur;if(S.o.keys)sfx('ding');if(S.o.letter){S.acc+=S.cur+'\n\n';S.shown=''}paint();
 if(S.q.length){if(S.o.auto)S.tm=setTimeout(adv,S.o.auto)}else{const f=S.cb;S.cb=null;f&&f()}}
function rev(){clearTimeout(S.tm);if(S.ty){clearInterval(S.ty);S.ty=null;S.shown=S.cur;if(S.o.letter){S.acc+=S.cur+'\n\n';S.shown=''}}
 while(S.q.length){const t=S.q.shift();S.cur=t;if(S.o.letter)S.acc+=t+'\n\n';else S.shown=t}S.pc=99;paint();const f=S.cb;S.cb=null;f&&f()}
// efeitos
function heart(x,y,c){x=rd(x);y=rd(y);rect(c,x+1,y,1,1);rect(c,x+3,y,1,1);rect(c,x,y+1,5,1);rect(c,x+1,y+2,3,1);rect(c,x+2,y+3,1,1)}
function fx(t,x,y){if(RM)return;for(let i=0;i<(t=='h'?5:8);i++)S.parts.push({t,x:x+Math.random()*10-5,y,vx:(Math.random()-.5)*.6,vy:-(.3+Math.random()*.5),t0:performance.now(),life:1400})}
function parts(now){S.parts=S.parts.filter(p=>now-p.t0<p.life);for(const p of S.parts){const a=(now-p.t0)/p.life,x=p.x+p.vx*(now-p.t0)/16,y=p.y+p.vy*(now-p.t0)/16;if(p.t=='h')heart(x,y,a<.7?'#d62839':'#a8142a');else rect(a<.6?'#ffd97a':'#f2a93b',x,y,1+(a<.3),1+(a<.3))}}
const SC={};function stars(r,now,n=26){const k=r.join();let a=SC[k];if(!a){let sd=r[0]*7+r[1]+3;const q=()=>(sd=sd*16807%2147483647)/2147483647;a=SC[k]=Array.from({length:n},()=>({x:rd(r[0]+q()*(r[2]-r[0])),y:rd(r[1]+q()*(r[3]-r[1])),p:q()*6,b:q()<.2})).filter(s=>!r[4]||(s.x<166||s.x>169))}
 for(const s of a)if(RM||((now/650+s.p)%3)<2.3){rect('#f0e2c0',s.x,s.y,1,1);if(s.b){rect('#8a8fa8',s.x-1,s.y,3,1);rect('#8a8fa8',s.x,s.y-1,1,3)}}}
const AMB=[];function ambient(now,col){if(RM)return;while(AMB.length<16)AMB.push({x:Math.random()*W,y:60+Math.random()*110,p:Math.random()*9,s:.2+Math.random()*.3});for(const a of AMB){a.y-=a.s*.3;a.x+=Math.sin(now/900+a.p)*.2;if(a.y<30){a.y=172;a.x=Math.random()*W}rect(col[a.p<4?0:1],a.x,a.y,1+(Math.sin(now/300+a.p)>.6),1)}}
const MO=[];function paper(x,y){spr('paper',x,y);const rows=Math.min(7,Math.ceil(S.pc/14));for(let l=0;l<rows;l++)rect('#5a5f78',x+3,y+6+l*3,l<rows-1?16:Math.min(16,Math.max(2,rd((S.pc-l*14)*16/14))),1)}
function roomProps(o={}){const now=E.now,T=M.typewriter,ty=122-T.h,tx=192-(T.w>>1),bs=n=>122-M[n].h;
 stars([126,22,210,48,1],now,18);spr('cat',97,bs('cat'));spr('mug',221,bs('mug'));spr('plant',288,bs('plant'));spr('monitor',246,bs('monitor'),rd(now/520)%2);spr('clock',236,40);
 if(o.dark)rect('rgba(10,14,31,.8)',0,0,W,H);paper(tx+11,ty-22);spr('typewriter',tx,ty,(now-S.lk<90&&S.ty&&S.o.keys)?S.kf:0);spr('lamp',124,bs('lamp'));spr('glow',87,bs('lamp')-16);
 if(!RM){if(Math.random()<.04&&MO.length<9)MO.push({x:128+Math.random()*10,y:106,t:now,d:(Math.random()-.5)*.6});
  for(let i=MO.length-1;i>=0;i--){const m=MO[i],a=(now-m.t)/3200;if(a>1){MO.splice(i,1);continue}rect(a<.7?'#ffd97a':'#f2a93b',m.x+Math.sin(a*6)*3+m.d*a*20,m.y-a*40,1,1)}}}
const sprS=(n,x,y,f,s,ch)=>{const m=M[n],h=ch||m.h;g.drawImage(IM[n],f*m.w,0,m.w,h,rd(x),rd(y+(m.dy||0)*s),m.w*s,h*s)};
const GL={P:["XXX","X.X","XXX","X..","X.."],'1':[".X.","XX.",".X.",".X.","XXX"],'2':["XXX","..X","XXX","X..","XXX"]};
function badge(t,x,y){rect('#0a0e1f',x-1,y-1,13,11);rect('#d62839',x,y,11,9);[...t].forEach((c,i)=>GL[c].forEach((r,j)=>[...r].forEach((p,k)=>{if(p=='X')rect('#f0e2c0',x+2+i*4+k,y+2+j,1,1)})))}
const E={S,M,spr,sprS,dy:n=>M[n].dy||0,badge,rect,blink:()=>RM?0:(E.now%4300<140?2:0),hopY:n=>(S.hop[n]&&E.now-S.hop[n]<420)?-Math.round(Math.sin((E.now-S.hop[n])/420*Math.PI)*5):0,stars,ambient,paper,roomProps,now:0,
 b:n=>RM?0:Math.floor((E.now+n)/700)%2,f:n=>RM?0:(E.now%4300<140?2:Math.floor((E.now+n)/700)%2),
 reveal(){S.reveal=.01;fx('s',150,100)},give(){S.give=1;S.hx=60},
 makeHeart(cx,cy){const P=["..XXX.XXX..",".XXXXXXXXX.","XXXXXXXXXXX","XXXXXXXXXXX",".XXXXXXXXX.","..XXXXXXX..","...XXXXX...","....XXX....",".....X....."];S.hp=[];
  P.forEach((r,j)=>[...r].forEach((c,i)=>{if(c=='X')S.hp.push({tx:cx-16+i*3,ty:cy+j*3,sx:cx-70+Math.random()*140,sy:cy+60+Math.random()*50,c:Math.random()<.2?'#ffd97a':Math.random()<.5?'#d62839':'#a8142a',d:Math.random()*500})}));S.hp.t0=performance.now();sfx('heart')},
 hearts(now){if(!S.hp)return;for(const p of S.hp){const a=Math.min(1,Math.max(0,(now-S.hp.t0-p.d)/1400)),e=1-Math.pow(1-a,3);rect(a<1||(now/300+p.tx)%7>=1?p.c:'#ffd97a',p.sx+(p.tx-p.sx)*e,p.sy+(p.ty-p.sy)*e,2,2)}}};
// fases
const txt=(s,h)=>CT.t[s.k][h.id],complete=s=>s.need?s.need.every(i=>S.found[i]):Object.keys(S.found).length>=s.needN;
function hud(){const s=ST[S.i];$('#ph').textContent='FASE '+String(s.n).padStart(2,'0')+'/'+CT.total;$('#tt').textContent=s.title;const sg=$('#seg');sg.innerHTML='';for(let i=1;i<=CT.total;i++){const e=document.createElement('i');if(i<=s.n)e.className='on';sg.append(e)}}
function load(i){clearTimeout(S.tm);clearTimeout(S.tm2);clearInterval(S.ty);Object.assign(S,{i,found:{},q:[],cb:null,o:{},ty:null,shown:'',acc:'',pc:0,script:ST[i].script||null,si:0,wait:false,end:false,done:false,fin:false,parts:[],wp:0,reveal:0,give:0,hx:60,hp:null,hop:{}});
 const s=ST[i];hud();$('#act').hidden=true;$('#back').hidden=i==0;localStorage.setItem('npu_stage',i);
 const h=$('#hsl');h.innerHTML='';(s.hs||[]).forEach(o=>{const b=document.createElement('button');b.textContent=o.l;b.onclick=()=>{if(!busy()&&!S.tr)press(o)};h.append(b)});
 S.fi=0;drawFace();const T=CT.t[s.k];say([T.intro,...(T.hint?[T.hint]:[])])}
function press(h){const s=ST[S.i];S.fi=[1,0,3,1,4,0,3][Object.keys(S.found).length%7];drawFace();sfx('select');if(h.note!=null)sfx('note',h.note);
 if(h.go=='zoom'){S.found[h.id]=1;say([txt(s,h)],()=>go(S.i+1,'zoom',h.x+h.w/2,h.y+h.h/2));return}
 if(h.type||h.letter){S.pc=0;say(h.letter?CT.letter:[h.type],()=>{S.found[h.id]=1;check()},h.letter?{keys:1,letter:1,auto:900}:{keys:1});return}
 S.found[h.id]=1;if(h.fx){if(h.fx.includes('h'))fx('h',h.x+h.w/2,h.y);if(h.fx.includes('s'))fx('s',h.x+h.w/2,h.y);if(h.hop)S.hop[h.hop]=performance.now()}
 const lines=[txt(s,h)];if(complete(s)&&s.final&&!S.fin){S.fin=true;lines.push(...s.final)}say(lines,check)}
function check(){if(!S.done&&complete(ST[S.i])&&!S.q.length)finish()}
function finish(){S.done=true;S.end=true;sfx('done');const a=$('#act');a.textContent=S.i==ST.length-1?'Reviver nossa história':'Próxima fase ▶';a.hidden=false;paint()}
function nextScript(){const it=S.script[S.si++],last=S.si>=S.script.length;
 if(typeof it=='string')say([it],last?finish:null);else if(it.type){S.pc=0;say([it.type],last?finish:null,{keys:1})}
 else{E[it.fn](it);S.wait=true;paint();S.tm2=setTimeout(()=>{S.wait=false;last?finish():nextScript()},it.wait||1000)}}
function tap(){if(S.mode!='play'||S.tr)return;if(S.ty){endLine();return}if(S.q.length){adv();return}if(S.script&&!S.wait&&!S.end)nextScript()}
function go(i,kind='d',cx=160,cy=90){if(!S.tr){sfx('whoosh');S.tr={t0:performance.now(),out:true,kind,cx,cy,next:i}}}
$('#act').onclick=()=>go(S.i==ST.length-1?0:S.i+1);$('#back').onclick=()=>go(S.i-1);$('#skip').onclick=rev;dlg.onclick=tap;
cv.onclick=e=>{if(S.mode!='play')return;if(S.tr){S.tr.t0=-1e9;return}const r=cv.getBoundingClientRect(),x=(e.clientX-r.left-4)*W/(r.width-8),y=(e.clientY-r.top-4)*H/(r.height-8);
 if(busy()||S.wait){tap();return}const h=[...(ST[S.i].hs||[])].reverse().find(h=>x>=h.x&&x<h.x+h.w&&y>=h.y&&y<h.y+h.h);h?press(h):tap()};
addEventListener('keydown',e=>{if(e.key!='Enter'&&e.key!=' ')return;if(['BUTTON','INPUT'].includes(document.activeElement.tagName))return;e.preventDefault();S.mode=='title'?begin(0):tap()});
function begin(i){S.mode='play';$('#title').hidden=true;document.body.classList.add('play');$('#hud').style.visibility='visible';ac();music(S.snd);sfx('found');load(i);S.tr={t0:performance.now(),out:false,kind:'d'}}
const saved=+localStorage.getItem('npu_stage')||0;if(saved>0){$('#cont').hidden=false;$('#cont').textContent='Continuar (fase '+(saved+1)+')'}
$('#play').onclick=()=>begin(0);$('#capaimg').onclick=()=>begin(0);$('#cont').onclick=()=>begin(saved);
function fit(){const s=Math.max(1,Math.floor(Math.min((innerWidth-24)/(W+8),(innerHeight-320)/(H+8))));const w=(W)*s+8;cv.style.width=w+'px';cv.style.height=H*s+8+'px';document.querySelectorAll('#hud,#dlg,#stage').forEach(e=>e.style.width=w+'px');const k=Math.max(1,Math.floor(Math.min(innerWidth/384,innerHeight/512)));$('#capaimg').style.width=384*k+'px'}
addEventListener('resize',fit);fit();
// desenho
function drawHs(s,now){if(S.mode!='play')return;(s.hs||[]).forEach((h,i)=>{const f=S.found[h.id];
 if(h.spr)spr(h.spr,h.x,h.y+(RM?0:rd(Math.sin(now/500+i)*2)),rd(now/450+i)%2,null,f?.5:1);
 else if(!f){const o=RM?0:rd(now/420)%2,cx=h.x+h.w/2;rect('#ffd97a',cx-3,h.y-6+o,7,1);rect('#ffd97a',cx-2,h.y-5+o,5,1);rect('#ffd97a',cx-1,h.y-4+o,3,1);rect('#ffd97a',cx,h.y-3+o,1,1)}})}
function drawScene(s,now){E.now=now;g.drawImage(IM[s.bg],0,0);if(s.sky)stars(s.sky,now);s.draw(E,now);if(s.fg)g.drawImage(IM[s.fg],0,0);drawHs(s,now);if(s.after)s.after(E,now);parts(now)}
const BL=Array.from({length:240},Math.random),blocks=p=>{for(let i=0;i<240;i++)if(BL[i]<p)rect('#0a0e1f',(i%20)*16,Math.floor(i/20)*15,16,15)};
function titleScene(now){g.drawImage(IM.capa,0,0);stars([0,0,320,40],now,16);if(!RM&&Math.random()<.03)fx('h',60+Math.random()*200,150);parts(now)}
function frame(now){g.setTransform(1,0,0,1,0,0);if(S.mode=='title'){requestAnimationFrame(frame);return}const t=S.tr;
 if(t){const dur=RM?150:(t.out?(t.kind=='zoom'?900:550):450),p=Math.min(1,(now-t.t0)/dur);
  if(t.out){if(t.kind=='zoom'){g.save();const sc=1+p*2.2;g.translate(t.cx,t.cy);g.scale(sc,sc);g.translate(-t.cx,-t.cy);drawScene(ST[S.i],now);g.restore();rect('rgba(10,14,31,'+p*p+')',0,0,W,H)}else{drawScene(ST[S.i],now);blocks(p)}
   if(p>=1){load(t.next);S.tr={t0:now,out:false,kind:'d'}}}
  else{drawScene(ST[S.i],now);blocks(1-p);if(p>=1)S.tr=null}}
 else drawScene(ST[S.i],now);requestAnimationFrame(frame)}
$('#hud').style.visibility='hidden';ST[0].k&&say([]);requestAnimationFrame(frame);
})();
