"""Gera a pixel art 2D do projeto, pixel a pixel, em PNG com transparência.
Uso: python3 tools/build_assets.py  (cria assets/*, assets/manifest.js e a prévia)"""
from PIL import Image, ImageDraw
import json, os, random
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAL=dict(k0='#0a0e1f',sk='#0c1330',n1='#111a3a',nb='#16224a',n2='#1c2a5a',n3='#2e4080',r1='#4a0d1a',r2='#7a1426',r3='#a8142a',r4='#d62839',
 c1='#f0e2c0',c2='#cdb88f',a1='#f2a93b',a2='#ffd97a',w0='#3a2218',w0b='#42281c',w1='#4a2a1c',w2='#744430',w3='#9a6444',
 g1='#5a5f78',g2='#8a8fa8',s1='#f1c7a3',s2='#d49a7a',s3='#e08a7a',h1='#1f1a2e',sb='#b08a70')
C={k:tuple(int(v[i:i+2],16) for i in (1,3,5))+(255,) for k,v in PAL.items()}
MAPS={}
class Cv:
    m={}
    def k(s,c): return C[s.m.get(c,c)] if isinstance(c,str) else c
    def __init__(s,w,h): s.w,s.h=w,h; s.im=Image.new('RGBA',(w,h),(0,0,0,0)); s.d=ImageDraw.Draw(s.im)
    def p(s,x,y,c):
        if 0<=x<s.w and 0<=y<s.h: s.im.putpixel((x,y),s.k(c))
    def r(s,x0,y0,x1,y1,c): s.d.rectangle((x0,y0,x1,y1),fill=s.k(c))
    def rows(s,d,c):
        for y,(a,b) in d.items(): s.r(a,y,b,y,c)
    def art(s,rows,x,y,m):
        for j,l in enumerate(rows):
            for i,ch in enumerate(l):
                if ch in m: s.p(x+i,y+j,m[ch])
def outline(cv):
    o=Cv(cv.w+2,cv.h+2); px=cv.im.load(); o.im.paste(cv.im,(1,1))
    for y in range(cv.h):
        for x in range(cv.w):
            if px[x,y][3]==0:
                for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                    X,Y=x+dx,y+dy
                    if 0<=X<cv.w and 0<=Y<cv.h and px[X,Y][3]: o.p(x+1,y+1,'k0');break
    return o
HEAD={5:(8,15),6:(7,16),7:(6,17),8:(6,17),9:(6,17),10:(6,17),11:(6,17),12:(6,17),13:(6,17),14:(7,16),15:(7,16),16:(8,15),17:(9,14)}
def bulk(c,et=2,el=4,wd=2):
    px=c.im.load(); w,h=c.im.size; rows=[]
    for y in range(h):
        rows.append(y)
        if y==30: rows+=[30]*et
        if y==38: rows+=[38]*el
    o=Cv(w+2*wd,len(rows)); op=o.im.load()
    for ny,y in enumerate(rows):
        if y<20: cols=[None]*wd+list(range(w))+[None]*wd
        else:
            cols=[]
            for x in range(w):
                cols.append(x)
                if x in (11,12): cols+=[x]*wd
        for i,x in enumerate(cols):
            if x is not None: op[i,ny]=px[x,y]
    return o
def person(kind,b=0,blink=False,give=False,happy=False):
    c=Cv(44 if give else 24,46); c.m=MAPS.get(kind,{}); her=kind=='her'
    if her:  # cabelo vermelho, longo e liso (atrás)
        hr={3:(7,16),4:(5,18)}; hr.update({y:(4,19) for y in range(5,32)}); hr.update({32:(5,18),33:(6,17)})
        for y,(x0,x1) in hr.items():
            yy=y+(b if y<12 else 0); c.r(x0,yy,x1,yy,'r3'); c.r(x0,yy,x0+1,yy,'r1'); c.r(x1-1,yy,x1,yy,'r1')
        for y in range(9,30):
            if y%6<4: c.p(8,y,'r4'); c.p(15,y,'r4')
        c.r(7,34,10,34,'r1'); c.r(13,34,16,34,'r1')
    c.r(10,18,13,19,'s2')
    if her:
        c.r(8,20,15,20,'c1'); c.r(7,21,16,33,'c1'); c.r(15,21,16,33,'c2'); c.r(7,32,16,33,'n2')
        c.r(10,20,13,20,'s1'); c.r(11,21,12,21,'s1')
    else:
        c.r(5,20,18,33,'n3'); c.r(16,21,18,33,'n2'); c.r(5,32,18,33,'n2'); c.r(3,21,4,32,'n3'); c.r(19,21,20,32,'n2')
        c.r(8,19,15,20,'n2'); c.r(10,22,10,26,'c1'); c.r(13,22,13,26,'c1'); c.p(10,27,'c2'); c.p(13,27,'c2'); c.r(7,29,16,29,'n2')
    for x0,x1 in ((5,6),(17,18)) if her else ((3,4),(19,20)):
        c.r(x0,31 if her else 33,x1,33 if her else 35,'s1')
    lc='n2' if her else 'n1'; hl='n3' if her else 'n2'
    c.r(7,34,11,43,lc); c.r(12,34,16,43,lc); c.r(7,34,8,43,hl); c.r(12,34,13,43,hl)
    c.r(6,44,11,45,'c1' if her else 'g1'); c.r(12,44,17,45,'c1' if her else 'g1'); c.r(6,45,17,45,'c2' if her else 'g2')
    c.rows({y+b:v for y,v in HEAD.items()},'s1')
    for y,(x0,x1) in HEAD.items():
        if y>=9: c.p(x1,y+b,'s2')
    c.r(9,17+b,14,17+b,'s2')
    for x in (9,14):
        if blink: c.p(x,11+b,'k0')
        else: c.p(x,10+b,'k0'); c.p(x,11+b,'k0')
    c.p(12,13+b,'s2')
    if happy:
        for x in (9,14): c.p(x,10+b,'s1'); c.p(x,11+b,'s1')
        for x in (8,13): c.p(x,11+b,'k0'); c.p(x+1,10+b,'k0'); c.p(x+2,11+b,'k0')
    if her:
        c.p(8,13+b,'s3'); c.p(15,13+b,'s3'); c.p(9,14+b,'r2'); c.p(14,14+b,'r2'); c.r(10,15+b,13,15+b,'r2')
        for x in (8,9,10,13,14,15): c.p(x,9+b,'r1')
        c.rows({3+b:(7,16),4+b:(6,17),5+b:(6,17),6+b:(6,17)},'r3'); c.r(6,7+b,11,7+b,'r3'); c.r(14,7+b,17,7+b,'r3')
        c.r(6,8+b,7,8+b,'r3'); c.r(16,8+b,17,8+b,'r3'); c.r(9,4+b,13,4+b,'r4'); c.r(8,5+b,11,5+b,'r4')
        for y in range(12,31):
            c.r(5,y,7,y,'r3'); c.p(5,y,'r1'); c.r(16,y,18,y,'r3'); c.p(18,y,'r1')
            if y%5<3: c.p(6,y,'r4'); c.p(17,y,'r4')
        for y in range(9+b,12): c.p(6,y,'r3'); c.p(17,y,'r3')
        c.r(5,30,7,30,'r1'); c.r(16,30,18,30,'r1')
    else:
        c.rows({3+b:(7,16),4+b:(6,17),5+b:(6,17),6+b:(6,17),7+b:(6,9)},'h1'); c.r(11,7+b,14,7+b,'h1'); c.r(15,7+b,17,7+b,'h1')
        for x in (7,9,11,13,15): c.p(x,2+b,'h1')
        c.p(6,3+b,'h1'); c.p(17,3+b,'h1')
        c.r(9,4+b,11,4+b,'eh2'); c.p(8,5+b,'eh2'); c.r(6,8+b,6,9+b,'h1'); c.r(17,8+b,17,9+b,'h1')
        for y in (11,12): c.p(5,y+b,'s2'); c.p(18,y+b,'s2')
        c.r(8,8+b,9,8+b,'h1'); c.r(14,8+b,15,8+b,'h1')
        for x0 in (7,13):  # óculos de armação fina
            c.r(x0,9+b,x0+3,9+b,'gd'); c.p(x0,10+b,'gd'); c.p(x0+3,10+b,'lg'); c.p(x0,12+b,'lg'); c.p(x0+3,12+b,'lg')
        c.r(11,9+b,12,9+b,'h1'); c.p(8,10+b,'c1'); c.p(15,10+b,'c1')
        c.r(10,14+b,13,14+b,'h1'); c.r(11,16+b,12,16+b,'r2')  # bigode discreto e boca
        for x in range(7,17):
            for y in (15,16,17):
                if (x+y)%2==0 and not(11<=x<=12 and y==16): c.p(x,y+b,'sb')
    if give:
        c.d.rectangle((19,21,20,35),fill=(0,0,0,0)); c.r(19,23,31,25,'n3'); c.r(19,25,31,25,'n2'); c.r(32,23,34,26,'s1')
    if happy:
        c.r(4,26,6,28,'s1'); c.r(17,26,19,28,'s1')
    if kind=='him': c=bulk(c)
    return outline(c)
def tw_frames():
    out=[]; keys=[(0,1),(1,2),(0,6),(1,4),(0,3)]
    for f in range(1+len(keys)):
        c=Cv(44,30)
        c.r(2,5,41,5,'g2'); c.r(3,6,40,9,'g1'); c.r(3,6,40,6,'g2'); c.r(0,5,2,10,'a1'); c.r(41,5,43,10,'a1'); c.r(0,5,2,5,'a2'); c.r(41,5,43,5,'a2')
        c.r(3,10,40,14,'n3'); c.r(3,14,40,14,'n2')
        for y in range(15,27):
            x0=2-(y-15)//6; c.r(x0,y,43-x0,y,'n2'); c.r(x0,y,x0+1,y,'n3')
        c.r(1,27,42,29,'k0'); c.r(3,27,40,27,'n1')
        for i in range(9): c.r(6+4*i,17,7+4*i,18,'c1'); c.r(6+4*i,19,7+4*i,19,'c2')
        for i in range(8): c.r(8+4*i,21,9+4*i,22,'c1'); c.r(8+4*i,23,9+4*i,23,'c2')
        c.r(12,25,31,25,'c1'); c.r(12,26,31,26,'c2'); c.r(19,12,24,12,'r3')
        if f:
            row,col=keys[f-1]; x=(6+4*col) if row==0 else (8+4*col); y=17 if row==0 else 21
            c.r(x,y,x+1,y+2,'n2'); c.r(x,y+1,x+1,y+2,'a1'); c.p(x,y+1,'a2')
        out.append(c.im)
    return out
def paper():
    c=Cv(22,26); c.r(0,0,21,25,'c1'); c.r(20,0,21,25,'c2'); c.r(0,0,21,0,'c2'); c.r(0,1,3,1,'c2'); c.r(0,25,21,25,'c2'); return c.im
def monitor():
    fr=[]
    for f in range(2):
        c=Cv(40,36); c.r(0,0,39,29,'c2'); c.r(0,0,39,0,'c1'); c.r(0,0,0,29,'c1'); c.r(38,1,39,29,'g1'); c.r(1,29,39,29,'g1')
        c.r(3,2,36,25,'k0'); c.r(4,3,35,24,'n1')
        for y,l in ((6,15),(9,22),(12,10),(15,18)): c.r(7,y,7+l,y,'a1')
        c.r(7,6,9,6,'a2'); c.r(7,18,8,18,'a2')
        if f==0: c.r(11,17,12,19,'a2')
        c.art([".X.X.","XXXXX",".XXX.","..X.."],31,25,{'X':'r4'})
        c.r(16,30,23,33,'c2'); c.r(16,30,16,33,'c1'); c.r(10,34,29,35,'c2'); c.r(10,35,29,35,'g1')
        fr.append(c.im)
    return fr
def lamp():
    c=Cv(16,28); c.r(3,25,12,27,'g1'); c.r(3,25,12,25,'g2'); c.r(3,27,12,27,'k0'); c.r(7,14,8,24,'g2'); c.r(8,14,8,24,'g1')
    for y in range(6,14):
        x0=max(1,4-(y-6)//2); c.r(x0,y,15-x0,y,'r2'); c.r(x0,y,x0+1,y,'r3')
    c.r(1,13,14,13,'r1'); c.r(2,14,13,14,'a2'); c.r(4,15,11,15,'a1'); return c.im
def clock():
    c=Cv(20,9); c.r(0,0,19,8,'k0'); c.r(1,1,18,7,'n1')
    D={'2':["XXX","..X","XXX","X..","XXX"],'3':["XXX","..X","XXX","..X","XXX"],'4':["X.X","X.X","XXX","..X","..X"],'7':["XXX","..X","..X","..X","..X"]}
    for x,d in ((2,'2'),(6,'3'),(12,'4'),(16,'7')): c.art(D[d],x,2,{'X':'a1'})
    c.p(10,3,'a2'); c.p(10,5,'a2'); return c.im
def books():
    c=Cv(20,12); c.r(0,8,19,11,'r2'); c.r(17,8,19,11,'c1'); c.r(0,9,16,9,'r1'); c.r(2,4,17,7,'n3'); c.r(15,4,17,7,'c2'); c.r(2,5,14,5,'n2'); c.r(1,0,14,3,'c2'); c.r(1,0,14,0,'c1'); c.r(12,0,14,3,'g1'); return c.im
def glow():
    c=Cv(90,64); B=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5]
    for y in range(64):
        for x in range(90):
            d=(((x-45)/45)**2+((y-32)/32)**2)**.5
            if d<1 and (1-d)*16>B[(y%4)*4+x%4]+5: c.p(x,y,(255,217,122,60) if d<.4 else (242,169,59,38))
    return c.im
def room():
    c=Cv(320,180); c.r(0,0,319,131,'n1')
    for x in range(0,320,16): c.r(x,0,x,125,'nb')
    c.r(0,126,319,131,'w1'); c.r(0,126,319,126,'w2')
    for y in range(132,180):
        c.r(0,y,319,y,'w0' if (y//8)%2==0 else 'w0b')
        if y%8==0: c.r(0,y,319,y,'k0')
        for x in range(((y//8)*37)%40,320,40): c.r(x,y,x,min(y+7,179),'k0')
    for y in range(132,140):
        for x in range(320):
            if (x+y)%2==0: c.p(x,y,'k0')
    c.r(12,146,132,178,'r1'); c.r(12,146,132,148,'r2'); c.r(12,176,132,178,'r2'); c.r(12,146,14,178,'r2'); c.r(130,146,132,178,'r2')
    for x in range(16,129,4): c.p(x,151,'c2'); c.p(x,173,'c2')
    c.r(120,16,215,91,'w3'); c.r(122,18,213,89,'w1')
    sky=[(20,35,'sk'),(36,51,'n1'),(52,67,'n2'),(68,87,'n3')]
    for y0,y1,col in sky: c.r(124,y0,211,y1,col)
    for i,(y0,y1,col) in enumerate(sky[1:]):
        for x in range(124,212):
            for yy in (y0,y0+1):
                if (x+yy)%2==0: c.p(x,yy,sky[i][2])
    rnd=random.Random(3)
    for lay,(col,hmin,hmax) in enumerate((('n2',8,20),('k0',10,30))):
        x=124
        while x<212:
            w=rnd.randint(6,12); h=rnd.randint(hmin,hmax); c.r(x,88-h,min(x+w-1,211),87,col)
            if lay:
                for yy in range(88-h+2,86,3):
                    for xx in range(x+1,min(x+w-1,211),2):
                        if rnd.random()<.2: c.p(xx,yy,rnd.choice(['a1','a2','a1','c1']))
            x+=w
    c.d.ellipse((184,24,194,34),fill=C['c1']); c.d.ellipse((187,22,197,32),fill=C['sk'])
    c.r(167,20,168,87,'w3'); c.r(124,52,211,53,'w3'); c.r(167,20,167,87,'w2')
    c.r(116,92,219,93,'w3'); c.r(116,94,219,95,'w2')
    c.r(16,74,100,76,'w2'); c.r(16,74,100,74,'w3'); c.r(18,77,98,78,'k0')
    x=18
    for w,h,col in ((4,16,'r2'),(3,13,'n3'),(4,15,'c2'),(3,12,'r3'),(5,16,'n2'),(3,14,'g1'),(4,11,'r1')):
        c.r(x,73-h,x+w-1,73,col); c.r(x,73-h,x,73,'k0' if col!='c2' else 'c1'); x+=w
    c.art(["..XXXXXXXXXX..",".XXXXXXXXXXXX.","XXgXXXXXXXrXXX","XgggXXXXXXXrXX",".XXXXXXXXXXXX.","..XXXXXXXXXX.."],70,68,{'X':'g1','g':'g2','r':'r4'})
    c.art(["XXXXXX","XccccX","XccaaX","XXXXXX"],56,70,{'X':'k0','c':'g2','a':'a1'})
    c.r(92,122,308,122,'w3'); c.r(92,123,308,126,'w2'); c.r(92,127,308,127,'w1')
    c.r(98,128,103,152,'w2'); c.r(98,128,98,152,'w3'); c.r(240,128,302,152,'w2'); c.r(240,128,302,128,'w1')
    for y in (130,140): c.r(244,y,298,y+8,'w1'); c.r(245,y+1,297,y+7,'w2'); c.r(268,y+3,274,y+4,'a1')
    for x in range(98,304):
        if x%2==0: c.p(x,153,'k0')
    for x0 in (36,64):
        for y,(a,b) in {155:(5,19),156:(2,22),157:(5,19)}.items():
            for x in range(x0+a,x0+b):
                if (x+y)%2==0: c.p(x,y,'k0')
    return c.im
def sheet(fr,w,h):
    im=Image.new('RGBA',(w*len(fr),h),(0,0,0,0))
    for i,f in enumerate(fr): im.paste(f,(i*w,0))
    return im
def save(im,p): im.save(os.path.join(R,p)); return p
def main():
    S={}
    for k,n in (('him','eu'),('her','karollyne')):
        fr=[person(k,0).im,person(k,1).im,person(k,0,True).im]; fw,fh=fr[0].size; S[n]=dict(src=save(sheet(fr,fw,fh),f'assets/sprites/{n}.png'),w=fw,h=fh,n=3,dy=48-fh)
    t=tw_frames(); S['typewriter']=dict(src=save(sheet(t,44,30),'assets/sprites/typewriter.png'),w=44,h=30,n=len(t))
    S['monitor']=dict(src=save(sheet(monitor(),40,36),'assets/sprites/monitor.png'),w=40,h=36,n=2)
    for n,f,w,h in (('paper',paper(),22,26),('lamp',lamp(),16,28),('clock',clock(),20,9),('books',books(),20,12)): S[n]=dict(src=save(f,f'assets/sprites/{n}.png'),w=w,h=h,n=1)
    S['glow']=dict(src=save(glow(),'assets/fx/lamp_glow.png'),w=90,h=64,n=1)
    S['room']=dict(src=save(room(),'assets/scenes/room_night.png'),w=320,h=180,n=1)
    open(os.path.join(R,'assets/manifest.js'),'w').write('window.MANIFEST='+json.dumps(S,indent=1)+';')
    ref=Image.new('RGBA',(190,62),(17,26,58,255))
    for j,k in enumerate(('karollyne','eu')): ref.alpha_composite(Image.open(os.path.join(R,S[k]['src'])),(4+j*92,6))
    ref.resize((ref.width*6,ref.height*6),Image.NEAREST).save(os.path.join(R,'assets/reference/ficha_personagens_x6.png'))
    pal=Image.new('RGBA',(len(PAL)*8,8))
    for i,k in enumerate(PAL): pal.paste(C[k],(i*8,0,i*8+8,8))
    pal.resize((pal.width*4,32),Image.NEAREST).save(os.path.join(R,'assets/reference/paleta.png'))
    sc=Image.open(os.path.join(R,S['room']['src'])).copy()
    def put(n,x,y,f=0):
        im=Image.open(os.path.join(R,S[n]['src'])); w=S[n]['w']; sc.alpha_composite(im.crop((f*w,0,f*w+w,S[n]['h'])),(x,y))
    put('paper',181,74); put('typewriter',170,92); put('monitor',240,86); put('lamp',124,94); put('books',284,110); put('clock',236,40)
    put('glow',87,78); p=ImageDraw.Draw(sc)
    for k,l in enumerate((14,16,9,16,6)): p.line((184,80+k*3,184+l,80+k*3),fill=C['g1'][:3])
    put('eu',36,108); put('karollyne',64,108)
    sc.save(os.path.join(R,'assets/reference/pilot_preview_1x.png')); sc.resize((960,540),Image.NEAREST).save(os.path.join(R,'assets/reference/pilot_preview_x3.png'))
if __name__=='__main__': main()
