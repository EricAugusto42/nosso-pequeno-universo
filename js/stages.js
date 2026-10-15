(()=>{const T=CONTENT.t,TW={id:'maquina',x:166,y:78,w:52,h:46,l:'Máquina de escrever'},LAMP={id:'abajur',x:122,y:84,w:30,h:40,l:'Abajur'};
const AN=(n,k,ox,oy,sc)=>{const a=MANIFEST[n].a[k];return{x:ox+a[0]*sc,y:oy+a[1]*sc,w:a[2]*sc,h:a[3]*sc}};
const room=E=>{E.roomProps();E.spr('eu',36,108,E.f(0));E.spr('karollyne',64,108,E.f(350))};
const star=(id,x,y,l)=>({id,spr:'ico_star',x,y,w:14,h:14,l});
const walk=(E,now)=>{const S=E.S;S.wp+=(S.si-S.wp)*.03;const mv=Math.abs(S.si-S.wp)>.03,f=mv?2+Math.floor(now/260)%2:E.b(0),cxf=y=>238-(y-96)*1.96;
 if(S.wp<2){const fy=152-S.wp*12,cx=cxf(fy),y=fy-48;E.spr('karollyne_b',cx-25,y,f);E.spr('eu_b',cx-1,y,f)}
 else{const fy=128-(S.wp-2)*9,cx=cxf(fy),y=fy-25;E.spr('karollyne_bs',cx-14,y,f);E.spr('eu_bs',cx,y,f)}};
const NP=[[40,40],[84,26],[128,16],[172,16],[216,26],[260,40]],IC=['ico_star','ico_heart','ico_smile','ico_compass','ico_star','ico_heart'];
const duo=E=>{E.sprS('karollyne',100,66+E.hopY('karollyne'),E.f(0),2);E.sprS('eu',170,66+E.hopY('eu'),E.f(350),2)};
window.STAGES=[
{k:'s1',title:'Uma noite diferente',bg:'beach',sky:[0,0,320,56],need:['janela'],
 hs:[{id:'lua',x:244,y:6,w:24,h:22,l:'Lua'},{id:'predios',x:236,y:60,w:70,h:34,l:'Prédios'},{id:'casal',x:130,y:90,w:60,h:50,l:'Nós dois'},{id:'janela',x:194,y:50,w:18,h:20,go:'zoom',l:'Janela iluminada'}],
 draw:E=>{E.spr('karollyne_b',132,94,E.b(0));E.spr('eu_b',158,94,E.b(350))}},
{k:'s2',title:'As palavras que estou escrevendo',bg:'room',need:['maquina'],hs:[{...TW,type:T.s2.type},LAMP],draw:room},
{k:'s3',title:'O que eu queria te dizer',bg:'room',need:['maquina'],hs:[{...TW,letter:true}],draw:room},
{k:'s4',title:'Quatro coisas que admiro em você',bg:'room',need:['sorriso','personalidade','ao_seu_lado','futuro'],
 hs:[{id:'sorriso',spr:'ico_smile',x:36,y:28,w:14,h:14,l:'Seu sorriso'},{id:'personalidade',spr:'ico_star',x:92,y:42,w:14,h:14,l:'Sua personalidade'},{id:'ao_seu_lado',spr:'ico_heart',x:254,y:66,w:14,h:14,l:'Como me sinto ao seu lado'},{id:'futuro',spr:'ico_compass',x:284,y:26,w:14,h:14,l:'Tudo o que ainda vamos viver'}],draw:room},
{k:'s5',title:'Pequenos detalhes, grandes sentimentos',bg:'room',needN:4,final:[T.s5.main],
 hs:[{id:'relogio',x:234,y:38,w:24,h:13,l:'Relógio'},LAMP,{id:'livros',x:16,y:55,w:32,h:20,l:'Livros'},{id:'controle',x:66,y:64,w:22,h:14,l:'Controle de videogame'},{id:'janela',x:122,y:18,w:92,h:52,l:'Janela'},{id:'monitor',x:246,y:92,w:44,h:32,l:'Computador'},{id:'gato',x:97,y:94,w:28,h:30,l:'Gatinho'},{id:'caneca',x:221,y:98,w:27,h:26,l:'Caneca'},{id:'planta',x:288,y:94,w:22,h:30,l:'Planta'}],draw:room},
{k:'fichaK',title:'Jogadora 1: Karollyne',bg:'frame',face:'k',need:['cabelo','olhos','sorriso','pele','classe'],final:[T.fichaK.main],
 hs:[{id:'cabelo',...AN('her_bust','cabelo',70,6,1),l:'Cabelo'},{id:'olhos',...AN('her_bust','olhos',70,6,1),l:'Olhos'},{id:'sorriso',...AN('her_bust','sorriso',70,6,1),l:'Sorriso'},{id:'pele',...AN('her_bust','pele',70,6,1),l:'Pele'},star('classe',214,70,'Classe')],
 draw:(E,now)=>{E.sprS('her_bust',70,6,0,1);E.badge('P1',50,14);E.ambient(now,['#d62839','#ffd97a'])}},
{k:'vermelho',title:'O vermelho é a cor dela',bg:'frame',face:'k',need:['topo','mechas','sorriso'],final:[T.vermelho.main],
 hs:[{id:'topo',...AN('her_bust','cabelo',49,0,2),l:'Cabelo'},{id:'mechas',...AN('her_bust','mechas',49,0,2),l:'Mechas'},{id:'sorriso',...AN('her_bust','sorriso',49,0,2),l:'Sorriso'}],
 draw:(E,now)=>{E.sprS('her_bust',49,0,0,2,90);E.ambient(now,['#d62839','#ffd97a'])}},
{k:'s6',title:'O jeito que só você tem',bg:'garden',sky:[0,0,320,86],need:['flor','estrela','coracao'],final:[T.s6.main],
 hs:[{id:'flor',spr:'flor',x:72,y:112,w:11,h:18,l:'Flor vermelha'},star('estrela',150,44,'Estrela'),{id:'coracao',spr:'ico_heart',x:238,y:126,w:14,h:14,l:'Coração'}],
 draw:(E,now)=>E.ambient(now,['#ffd97a','#f2a93b'])},
{k:'s7',title:'Nosso jeito de ser',bg:'sofa',fg:'sofafg',need:['leveza','carinho','companheirismo'],final:[T.s7.main],
 hs:[{id:'carinho',x:133,y:90,w:26,h:38,fx:'h',hop:'karollyne',l:'Karollyne'},{id:'leveza',x:161,y:86,w:30,h:42,fx:'s',hop:'eu',l:'Eu'},{id:'companheirismo',x:150,y:112,w:14,h:14,fx:'hs',l:'Nossas mãos'}],
 draw:E=>{E.spr('karollyne',133,92+E.hopY('karollyne'),E.f(0),38);E.spr('eu',161,92+E.hopY('eu'),E.f(350),40)}},
{k:'ritmo',title:'Nosso ritmo',bg:'select',need:NP.map((_,i)=>'n'+i),final:[T.ritmo.main],
 hs:NP.map(([x,y],i)=>({id:'n'+i,spr:IC[i],x,y,w:14,h:14,l:'Nota '+(i+1),note:i,hop:i%2?'eu':'karollyne',fx:'s'})),draw:duo},
{k:'s8',title:'Nosso pequeno universo',bg:'city',fg:'cityfg',sky:[0,0,320,52],need:['carinho','confianca','companheirismo','futuro'],final:[T.s8.main],
 hs:[star('carinho',52,22,'Estrela: carinho'),star('confianca',112,40,'Estrela: confiança'),star('companheirismo',206,24,'Estrela: companheirismo'),star('futuro',282,52,'Estrela: nosso futuro')],
 draw:E=>{E.spr('karollyne_b',134,98,E.b(0),37);E.spr('eu_b',160,98,E.b(350),39)}},
{k:'s9',title:'Tudo o que ainda vamos viver',bg:'sunset',sky:[0,0,320,60],script:T.s9.lines,draw:walk},
{k:'conq',title:'Conquistas desbloqueadas',bg:'select',need:['a1','a2','a3','a4','a5'],final:[T.conq.main],
 hs:[[60,40],[110,24],[160,16],[210,24],[260,40]].map(([x,y],i)=>({id:'a'+(i+1),spr:IC[i],x,y,w:14,h:14,l:'Conquista '+(i+1),fx:'hs',hop:i%2?'eu':'karollyne'})),draw:duo},
{k:'s10',title:'Quem escreveu tudo isso?',bg:'room',script:[{type:T.s10.a},{type:T.s10.b},{fn:'reveal',wait:1800},T.s10.c,T.s10.d,T.s10.e],
 draw:(E,now)=>{const S=E.S;E.roomProps({dark:true});if(S.reveal>0){S.reveal=Math.min(1,S.reveal+.012);E.spr('eu',140,100,E.f(0),null,S.reveal)}E.ambient(now,['#d62839','#f2a93b'])}},
{k:'fichaE',title:'Jogador 2',bg:'frame',face:'e',need:['cabelo','oculos','bigode','porte','classe'],final:[T.fichaE.main],
 hs:[{id:'cabelo',...AN('him_bust','cabelo',70,3,1),l:'Cabelo'},{id:'oculos',...AN('him_bust','oculos',70,3,1),l:'Óculos'},{id:'bigode',...AN('him_bust','bigode',70,3,1),l:'Bigode'},{id:'porte',...AN('him_bust','porte',70,3,1),l:'Porte'},star('classe',214,70,'Classe')],
 draw:E=>{E.sprS('him_bust',70,3,0,1);E.badge('P2',50,14)}},
{k:'s11',title:'Quatro meses de nós',bg:'golden',script:[{fn:'give',wait:3200},T.s11.a,T.s11.b,T.s11.c,{type:T.s11.d}],
 draw:(E,now)=>{const S=E.S,M=E.M,T0=M.typewriter,ty=150-T0.h,GY=100,sd=M.eu_side,gv=M.eu_give,RX=106+gv.tip[0]+8;
  E.paper(255,ty-22);E.spr('typewriter',244,ty,(now-S.lk<90&&S.ty&&S.o.keys)?S.kf:0);
  if(S.give==1){S.hx=Math.min(106,S.hx+.55);if(S.hx>=106){S.give=2;E.makeHeart(140,32)}}
  if(S.give<2){E.spr('karollyne_side',RX+11,GY,E.b(350));E.spr('eu_side',S.hx,GY,S.give==1?Math.floor(now/160)%2:E.b(0));E.spr('bouquet',S.hx+sd.tip[0],GY+sd.dy+sd.tip[1])}
  else{E.spr('karollyne_rcv',RX,GY,E.b(350));E.spr('eu_give',106,GY,E.b(0));E.spr('bouquet',106+gv.tip[0],GY+gv.dy+gv.tip[1])}},
 after:(E,now)=>E.hearts(now)}];
STAGES.forEach((s,i)=>s.n=i+1);CONTENT.total=STAGES.length;
})();
