"""Cenários, poses e ícones das 11 fases. Uso: python3 tools/build_scenes.py (roda tudo)."""
import math, json, random, build_assets as B
from build_assets import *
PAL.update(gd='#0f2f36',gr='#1d4a45',gl='#2f7a62')
for k in('gd','gr','gl'): C[k]=tuple(int(PAL[k][i:i+2],16) for i in (1,3,5))+(255,)
def sky(c,y1,cols):
    n=len(cols); h=y1//n
    for i,col in enumerate(cols):
        c.r(0,i*h,319,((i+1)*h-1) if i<n-1 else y1,col)
        if i:
            for x in range(320):
                for yy in (i*h,i*h+1):
                    if (x+yy)%2==0: c.p(x,yy,cols[i-1])
SKY=['sk','n1','n2','n3']
def city():
    c=Cv(320,180); sky(c,120,SKY); c.d.ellipse((248,14,262,28),fill=C['c1']); c.d.ellipse((251,12,265,26),fill=C['sk'])
    rnd=random.Random(5)
    for col,hmin,hmax,lit in (('n2',20,60,0),('k0',30,85,1)):
        x=-4
        while x<320:
            w=rnd.randint(10,24); h=rnd.randint(hmin,hmax); c.r(x,140-h,x+w-1,140,col)
            if lit:
                for yy in range(140-h+4,136,5):
                    for xx in range(x+3,x+w-3,4):
                        if rnd.random()<.28: c.r(xx,yy,xx+1,yy+1,rnd.choice(['a1','a2','a1','c1']))
            x+=w+rnd.randint(0,3)
    c.r(188,56,224,140,'k0'); c.r(196,98,205,111,'k0'); c.r(197,99,204,110,'a2'); c.r(200,99,201,110,'k0'); c.r(197,104,204,104,'k0')
    for y in range(86,140,6): c.r(192,y,193,y+1,'a1'); c.r(216,y+2,217,y+3,'a1')
    fg=Cv(320,180); fg.r(0,134,319,179,'n1'); fg.r(0,134,319,134,'g2'); fg.r(0,135,319,138,'g1'); fg.r(0,139,319,139,'k0')
    for y in range(147,180,8):
        fg.r(0,y,319,y,'nb')
        for x in range((y//8%2)*10,320,20): fg.r(x,y-8,x,y,'nb')
    return c.im,fg.im
def garden():
    c=Cv(320,180); sky(c,110,SKY)
    for x in range(320): c.r(x,int(100+8*math.sin(x/37)+5*math.sin(x/13)),x,179,'n2')
    for x in range(320): c.r(x,int(116+6*math.sin(x/29+1)),x,179,'gd')
    for x in range(8,320,14): c.r(x,104,x+5,129,'w2'); c.r(x,104,x,129,'w3'); c.r(x,104,x+5,105,'w1')
    c.r(0,112,319,114,'w1'); c.r(0,122,319,124,'w1'); c.r(0,129,319,179,'gd')
    rnd=random.Random(9)
    for _ in range(140): x=rnd.randint(0,319); y=rnd.randint(131,178); c.r(x,y,x,y+2,'gr')
    for _ in range(55):
        x=rnd.randint(8,312); y=rnd.randint(134,174); c.r(x,y,x,y+3,'gr'); c.r(x-1,y-1,x+1,y,rnd.choice(['r4','r3','c1','a1','r4']))
    for i in range(0,320):
        y=8+int(20*(1-((i%160-80)/80)**2)); c.p(i,y,'k0')
        if i%12==0: c.r(i,y+1,i+1,y+2,'a1' if i%24 else 'a2')
    return c.im
def road():
    c=Cv(320,180); sky(c,96,SKY); rnd=random.Random(2)
    for x in range(320):
        h=int(90+3*math.sin(x/17)+2*math.sin(x/5)); c.r(x,h,x,179,'n2')
        if rnd.random()<.12: c.p(x,rnd.randint(90,95),'a1')
    for x in range(0,320,2): c.p(x,94,'a1') if x%8==0 else None
    c.r(0,96,319,179,'gd')
    for y in range(96,180):
        t=(y-96)/83; hw=int(5+t*110); c.r(160-hw,y,160+hw,y,'n1'); c.r(160-hw,y,160-hw+1+int(t*2),y,'g1'); c.r(160+hw-1-int(t*2),y,160+hw,y,'g1')
        if int(t*14)%2==0: c.r(159-int(t*2),y,160+int(t*2),y,'c2')
    for t in (.06,.18,.38,.7):
        y=96+int(t*83); hw=int(5+t*110); s=1+int(t*3)
        for side in (-1,1):
            x=160+side*(hw+6+int(t*14)); c.r(x,y-8*s,x,y,'g1'); c.r(x-s,y-9*s,x+s,y-8*s,'a2')
            for dx in range(-3*s,3*s+1):
                for dy in range(-3*s,3*s+1):
                    if (dx+dy)%2==0 and dx*dx+dy*dy<9*s*s and abs(dx)+abs(dy)>s: c.p(x+dx,y-9*s+dy,(242,169,59,255))
    return c.im
def final():
    c=Cv(320,180); sky(c,112,SKY); rnd=random.Random(4)
    for x in range(320):
        h=int(104+6*math.sin(x/31)+3*math.sin(x/9)); c.r(x,h,x,179,'n2')
        if rnd.random()<.2: c.p(x,rnd.randint(h+1,h+6),'a1')
    for x in range(320): c.r(x,int(118+4*math.sin(x/23+2)),x,179,'gd')
    for _ in range(170): x=rnd.randint(0,319); y=rnd.randint(124,178); c.r(x,y,x,y+2,'gr')
    for _ in range(80):
        x=rnd.randint(4,316); y=rnd.randint(128,176); c.r(x,y,x,y+3,'gr'); c.r(x-1,y-1,x+1,y,rnd.choice(['r4','r3','c1','a1','a2']))
    c.r(226,150,318,151,'w3'); c.r(226,152,318,155,'w2'); c.r(226,156,318,179,'w1'); c.r(230,156,234,179,'w2'); c.r(310,156,314,179,'w2')
    return c.im
def sofa():
    c=Cv(320,180); c.r(0,0,319,131,'n1')
    for x in range(0,320,16): c.r(x,0,x,125,'nb')
    c.r(0,126,319,131,'w1'); c.r(0,126,319,126,'w2')
    for y in range(132,180):
        c.r(0,y,319,y,'w0' if (y//8)%2==0 else 'w0b')
        if y%8==0: c.r(0,y,319,y,'k0')
    c.r(24,22,72,70,'w3'); c.r(26,24,70,68,'w1'); c.r(28,26,68,66,'sk')
    rnd=random.Random(1)
    for _ in range(14): c.p(rnd.randint(30,66),rnd.randint(28,64),'c1')
    c.d.ellipse((52,32,60,40),fill=C['c1']); c.d.ellipse((54,31,62,39),fill=C['sk'])
    for i in range(0,320,4):
        y=10+int(8*math.sin(i/320*math.pi*4)); c.p(i,y,'k0')
        if i%16==0: c.r(i,y+1,i+1,y+2,'a1' if i%32 else 'a2')
    c.r(262,64,263,140,'g1'); c.r(256,44,269,50,'r2'); c.r(258,50,267,58,'r2'); c.r(257,59,268,59,'a2'); c.r(254,140,268,142,'g1')
    c.r(96,132,224,150,'r1'); c.r(110,92,210,132,'r2'); c.r(110,92,210,94,'r3'); c.r(112,96,158,128,'r1'); c.r(162,96,208,128,'r1')
    c.r(12,150,150,178,'n3'); c.r(12,150,150,152,'n2'); c.r(170,150,308,178,'n3')
    fg=Cv(320,180); fg.r(92,104,110,150,'r2'); fg.r(92,104,110,106,'r3'); fg.r(210,104,228,150,'r2'); fg.r(210,104,228,106,'r3'); fg.r(92,104,92,150,'r1'); fg.r(228,104,228,150,'r1')
    fg.r(110,122,210,150,'r2'); fg.r(110,122,210,124,'r3'); fg.r(110,146,210,150,'r1'); fg.r(158,124,159,146,'r1')
    fg.r(96,150,100,156,'w1'); fg.r(220,150,224,156,'w1'); fg.r(151,119,161,122,'k0'); fg.r(152,120,160,121,'s1')
    return c.im,fg.im
def back(kind,b=0,la=0,lb=0):
    c=Cv(24,46); c.m=MAPS.get(kind,{}); her=kind=='her'
    if her:
        hr={3:(7,16),4:(5,18)}; hr.update({y:(4,19) for y in range(5,32)}); hr.update({32:(5,18),33:(6,17)})
        for y,(x0,x1) in hr.items():
            yy=y+(b if y<12 else 0); c.r(x0,yy,x1,yy,'r3'); c.r(x0,yy,x0+1,yy,'r1'); c.r(x1-1,yy,x1,yy,'r1')
        for y in range(8,30):
            if y%6<4: c.p(8,y,'r4'); c.p(15,y,'r4')
            if y%7<3: c.p(11,y,'r4')
        c.r(9,4+b,13,4+b,'r4'); c.r(7,34,10,34,'r1'); c.r(13,34,16,34,'r1')
        for x0 in (3,20): c.r(x0,31,x0+1,34,'s1')
    else:
        c.rows({3+b:(7,16),4+b:(6,17)},'h1'); c.r(6,5+b,17,14+b,'h1'); c.r(9,4+b,11,4+b,'n3'); c.p(8,6+b,'n3')
        for y in (10,11): c.p(5,y+b,'s2'); c.p(18,y+b,'s2')
        c.r(10,15+b,13,19,'s2'); c.r(5,20,18,33,'n3'); c.r(16,21,18,33,'n2'); c.r(5,32,18,33,'n2'); c.r(3,21,4,32,'n3'); c.r(19,21,20,32,'n2')
        c.r(7,18,16,23,'n2'); c.r(9,20,14,21,'n3'); c.r(3,33,4,35,'s1'); c.r(19,33,20,35,'s1')
    lc='n2' if her else 'n1'; sh='c1' if her else 'g1'
    c.r(7,34,11,43-la,lc); c.r(12,34,16,43-lb,lc); c.r(6,44-la,11,45-la,sh); c.r(12,44-lb,17,45-lb,sh)
    return c
def half(cv):
    w,h=cv.im.size; s=Cv(w//2,h//2); s.im=cv.im.resize((w//2,h//2),Image.NEAREST); s.d=ImageDraw.Draw(s.im); return s
def icon(n,f):
    c=Cv(14,14)
    if n=='smile':
        c.d.ellipse((1,1,12,12),fill=C['a1']); c.d.ellipse((2,2,11,11),fill=C['a2']); c.r(4,5,4,6,'k0'); c.r(9,5,9,6,'k0') if f==0 else c.r(8,6,9,6,'k0')
        c.r(5,9,8,9,'k0'); c.p(3,8,'k0'); c.p(10,8,'k0')
    elif n=='star':
        c.r(6,1,7,12,'a1'); c.r(1,6,12,7,'a1'); c.r(5,4,8,9,'a2'); c.r(4,5,9,8,'a2'); c.r(6,6,7,7,'c1')
        if f: [c.p(x,y,'a2') for x,y in((3,3),(10,3),(3,10),(10,10))]
    elif n=='heart':
        y0=3-f; c.art(["..XX.XX..",".XXXXXXX.","XXXXXXXXX","XXXXXXXXX",".XXXXXXX.","..XXXXX..","...XXX...","....X...."],2,y0,{'X':'r4' if not f else 'r3'}); c.p(3,y0+2,'c1')
        if f: c.p(0,1,'a2'); c.p(13,2,'a2')
    else:
        c.d.ellipse((1,1,12,12),fill=C['c2']); c.d.ellipse((2,2,11,11),fill=C['n1'])
        if f==0: c.r(6,3,7,6,'r4'); c.r(6,7,7,10,'c1')
        else: c.p(9,3,'r4'); c.p(8,4,'r4'); c.p(7,5,'r4'); c.p(6,6,'c1'); c.p(5,7,'c1'); c.p(4,8,'c1'); c.p(6,5,'r4')
    return c.im
def flor(f):
    c=Cv(11,18); c.r(5,9,5,17,'gl'); c.r(2,13,4,13,'gr'); c.r(6,11,8,11,'gr')
    for y in range(0,9):
        for x in range(11):
            if (x-5)**2+(y-4)**2<=16: c.p(x,y,'r4' if (x+y)%7 else 'r3')
    c.r(4,3,6,5,'a1'); c.p(5,4,'a2')
    if f: c.p(0,0,'a2'); c.p(10,1,'a2'); c.p(1,8,'a2')
    return c.im
def bouquet():
    c=Cv(12,16)
    for y,(a,b) in {8:(1,10),9:(1,10),10:(2,9),11:(2,9),12:(3,8),13:(3,8),14:(4,7),15:(5,6)}.items(): c.r(a,y,b,y,'c1'); c.p(a,y,'c2')
    c.r(3,12,8,12,'r3'); c.r(0,6,2,8,'gr'); c.r(9,6,11,8,'gr'); c.r(4,7,7,7,'gl')
    for cx,cy in((3,4),(8,3),(6,6),(10,6)): c.r(cx-1,cy-1,cx+1,cy+1,'r4'); c.r(cx-1,cy-2,cx+1,cy-2,'r4'); c.p(cx,cy,'r1'); c.p(cx+1,cy+1,'r3')
    for x,y in((1,3),(11,2),(5,1)): c.p(x,y,'c1'); c.p(x+1,y,'a1')
    return c.im
def select(plat=True):
    c=Cv(320,180); sky(c,180,['sk','n1','n2']); B=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5]
    for y in range(180):
        for x in range(320):
            d=(((x-160)/120)**2+((y-165)/150)**2)**.5
            if d<1 and (1-d)*16>B[(y%4)*4+x%4]+4: c.p(x,y,'n3')
    rnd=random.Random(8)
    for _ in range(26): c.p(rnd.randint(60,260),rnd.randint(18,90),'c1')
    for x in range(0,52):
        col='r2' if (x//6)%2==0 else 'r1'; c.r(x,0,x,179,col); c.r(319-x,0,319-x,179,col)
    for y in range(180):
        for x in (52,53,54,55,264,265,266,267):
            if (x+y)%2==0: c.p(x,y,'k0')
    c.r(0,0,319,10,'r2')
    for x in range(0,320,20): c.d.ellipse((x,2,x+19,20),fill=C['r2']); c.d.arc((x,2,x+19,20),0,180,fill=C['r1'])
    if plat: c.d.ellipse((66,152,254,180),fill=C['k0']); c.d.ellipse((66,146,254,174),fill=C['n2']); c.d.ellipse((74,148,246,168),fill=C['n3'])
    return c.im
def build():
    S={}
    S2=lambda n,im,w,h,k=1:S.__setitem__(n,dict(src=save(im,f'assets/{"scenes" if w==320 else "sprites"}/{n}.png'),w=w,h=h,n=k))
    a,b=city(); S2('city',a,320,180); S2('cityfg',b,320,180); S2('garden',garden(),320,180); S2('road',road(),320,180); S2('final',final(),320,180)
    a,b=sofa(); S2('sofa',a,320,180); S2('sofafg',b,320,180); S2('select',select(),320,180)
    for k,n in(('him','eu'),('her','karollyne')):
        raw=[back(k,0),back(k,1),back(k,0,1,0),back(k,1,0,1)]
        S2(n+'_b',sheet([outline(r).im for r in raw],26,48),26*4,48,4)
        S2(n+'_bs',sheet([outline(half(r)).im for r in raw],14,25),14*4,25,4)
    S2('eu_give',sheet([person('him',0,False,True).im,person('him',1,False,True).im],46,48),92,48,2)
    S2('karollyne_rcv',sheet([person('her',0,False,False,True).im,person('her',1,False,False,True).im],26,48),52,48,2)
    for n in('smile','star','heart','compass'): S2('ico_'+n,sheet([icon(n,0),icon(n,1)],14,14),28,14,2)
    S2('flor',sheet([flor(0),flor(1)],11,18),22,18,2); S2('bouquet',bouquet(),12,16)
    # corrige larguras de quadro (w = largura de UM quadro)
    for n,w in(('eu_b',26),('karollyne_b',26),('eu_bs',14),('karollyne_bs',14),('eu_give',46),('karollyne_rcv',26),('ico_smile',14),('ico_star',14),('ico_heart',14),('ico_compass',14),('flor',11)): S[n]['w']=w
    return S
if __name__=='__main__':
    B.main(); import re
    p=os.path.join(R,'assets/manifest.js'); M=json.loads(open(p).read()[len('window.MANIFEST='):-1]); M.update(build())
    open(p,'w').write('window.MANIFEST='+json.dumps(M,indent=1)+';')
    sheetp=Image.new('RGBA',(640,540),(10,14,31,255))
    for i,n in enumerate(('city','garden','road','final')):
        im=Image.open(os.path.join(R,M[n]['src'])).copy()
        if n=='city': im.alpha_composite(Image.open(os.path.join(R,M['cityfg']['src'])))
        sheetp.alpha_composite(im,((i%2)*320,(i//2)*180))
    im=Image.open(os.path.join(R,M['sofa']['src'])).copy(); fr=lambda n,f:Image.open(os.path.join(R,M[n]['src'])).crop((f*M[n]['w'],0,f*M[n]['w']+M[n]['w'],M[n]['h']))
    im.alpha_composite(fr('karollyne',0).crop((0,0,26,38)),(133,92)); im.alpha_composite(fr('eu',0).crop((0,0,26,38)),(161,92)); im.alpha_composite(Image.open(os.path.join(R,M['sofafg']['src'])))
    sheetp.alpha_composite(im,(0,360)) if False else sheetp.alpha_composite(im.crop((0,0,320,180)),(0,360))
    im=Image.open(os.path.join(R,M['final']['src'])).copy(); im.alpha_composite(fr('eu_give',0),(106,100)); im.alpha_composite(fr('bouquet',0),(136,112)); im.alpha_composite(fr('karollyne_rcv',0),(146,100))
    sheetp.alpha_composite(im,(320,360)); sheetp.resize((1280,1080),Image.NEAREST).save(os.path.join(R,'assets/reference/cenarios_contato.png'))
    ic=Image.new('RGBA',(300,60),(10,14,31,255)); x=4
    for n in('ico_smile','ico_star','ico_heart','ico_compass','flor','bouquet','eu_b','karollyne_b','eu_bs','karollyne_bs'):
        ic.alpha_composite(fr(n,0),(x,6)); x+=M[n]['w']+6
    ic.resize((1200,240),Image.NEAREST).save(os.path.join(R,'assets/reference/sprites_novos_x4.png')); print('ok')
