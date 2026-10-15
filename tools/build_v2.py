"""Versão com a aparência real de vocês (fotos de referência): retratos, praia, pôr do sol, capa.
Uso: python3 tools/build_v2.py"""
import math, random, json
import build_assets as B, build_scenes as BS
from build_assets import *
from build_scenes import sky, half, back, icon, flor, bouquet
NEWC=dict(f1='#f6d5c3',f2='#dba592',f3='#e08a7a',lp='#c24244',lp2='#a8302f',lpl='#d4574f',hr1='#4a1418',hr2='#7a1d1f',hr3='#a82a24',hr4='#d2412f',
 e1='#c08560',e2='#aa7054',e3='#8a5a40',es='#684531',eh='#1b181a',eh2='#34302f',ep='#a45354',gd='#d6bf88',lg='#d8b79a',sw='#f4ece4',ir='#3e2218',lk='#2a1518',
 tc2='#9a5a44',tc3='#7a4234',po1='#1a1e30',po2='#2a3150',ln='#c68c66',dk1='#0c1330',dk2='#1c2a5a',dk3='#3e3a7a',dk4='#7a4a7a',dk5='#c8546a',
 sd1='#8a7a86',sd2='#6e6272',sd3='#a08e96',sn1='#2a2260',sn2='#6a2a7a',sn3='#b8406a',sn4='#e8603f',sn5='#f2a03b',sn6='#ffd97a',se1='#6a3a7a',se2='#8a4a7a',
 sa1='#e8b87a',sa2='#d49a62',sa3='#a8704a',gs1='#7aa0d8',gs2='#a8c0e0',gs3='#f0d8b0',gs4='#f8c88a',gs5='#f2a03b',gb1='#8a9ac0',gb2='#6a7aa8',gv1='#4a90b0',gv2='#3a7a9a',sg1='#e8c890',sg2='#d8b078',sg3='#b8905a',sun='#fff2c8')
PAL.update(NEWC); C.update({k:tuple(int(v[i:i+2],16) for i in (1,3,5))+(255,) for k,v in NEWC.items()})
B.MAPS.update({'her':{'s1':'f1','s2':'f2','s3':'f3','r1':'hr1','r3':'hr3','r4':'hr4','r2':'lp'},'him':{'s1':'e1','s2':'e2','sb':'es','h1':'eh','r2':'ep'}})
def mk(w,h,fn): m=Image.new('L',(w,h),0); fn(ImageDraw.Draw(m)); return m
def fm(c,m,fn):
    px=m.load()
    for y in range(m.height):
        for x in range(m.width):
            if px[x,y]: c.p(x,y,fn(x,y))
def hairc(x,y):
    t=(x*3+int(4*math.sin(y/7+x/4)))%7; col='hr4' if (t==0 and 12<y<66) else ('hr2' if t>=5 else 'hr3')
    return ('hr1' if t%2 else 'hr2') if (min(x,63-x)<5 or y>72) else col
def her_bust():
    c=Cv(64,80); fm(c,mk(64,80,lambda d:(d.ellipse((10,4,54,50),fill=255),d.polygon([(10,28),(54,28),(60,50),(62,80),(2,80),(4,50)],fill=255))),hairc)
    c.d.polygon([(6,80),(10,68),(22,62),(42,62),(54,68),(58,80)],fill=C['tc2']); c.d.polygon([(6,80),(10,68),(15,66),(14,80)],fill=C['tc3']); c.d.polygon([(58,80),(54,68),(49,66),(50,80)],fill=C['tc3'])
    c.r(27,48,37,64,'f2'); c.d.ellipse((27,58,37,66),fill=C['f1'])
    face=[(19,30),(20,20),(26,16),(38,16),(44,20),(45,30),(43,42),(38,50),(32,53),(26,50),(21,42)]
    fm(c,mk(64,80,lambda d:d.polygon(face,fill=255)),lambda x,y:'f2' if (x>=42 or y>=51 or (x>=40 and (x+y)%2==0)) else 'f1')
    for bx in (24,40):
        for dx in range(-3,4):
            for dy in range(-2,3):
                if dx*dx+dy*dy<=4 and (dx+dy+bx)%2==0: c.p(bx+dx,39+dy,'f3')
    fm(c,mk(64,80,lambda d:(d.polygon([(6,40),(20,44),(18,80),(4,80)],fill=255),d.polygon([(44,44),(58,40),(60,80),(46,80)],fill=255))),hairc)
    fm(c,mk(64,80,lambda d:d.polygon([(29,9),(17,22),(17,36),(21,36),(22,25),(29,15),(38,19),(43,27),(43,36),(47,36),(47,22),(40,11)],fill=255)),hairc)
    for cx in (26,38):
        for x in range(cx-3,cx+3): c.p(x,30,'lk') if x in (cx-3,cx+2) else c.p(x,29,'lk')
        for x in (cx-3,cx-2,cx+1,cx+2): c.p(x,31,'sw'); c.p(x,32,'sw')
        c.r(cx-1,31,cx,32,'ir'); c.p(cx,31,'sw'); c.r(cx-2,33,cx+1,33,'f2'); c.p(cx-4 if cx==26 else cx+3,30,'lk')
    for x,y in((21,26),(22,25),(23,25),(24,24),(25,24),(26,24),(27,24),(28,25),(36,25),(37,24),(38,24),(39,24),(40,24),(41,25),(42,25),(43,26)): c.p(x,y,'hr1')
    for y in range(31,37): c.p(34,y,'f2')
    for x,y in((30,39),(34,39),(31,40),(32,40),(33,40)): c.p(x,y,'f3' if y==39 else 'f2')
    c.r(28,44,36,44,'lp2'); c.p(26,44,'lp2'); c.p(38,44,'lp2'); c.r(27,45,28,45,'lp'); c.r(36,45,37,45,'lp'); c.r(29,45,35,45,'sw'); c.r(28,46,36,46,'lpl'); c.r(29,47,35,47,'lp'); c.p(25,45,'f2'); c.p(39,45,'f2')
    c.r(18,40,19,41,'sw'); return c,dict(cabelo=(12,4,40,24),olhos=(20,24,26,11),sorriso=(25,42,14,8),pele=(22,34,22,8),mechas=(2,34,16,24))
def him_bust():
    c=Cv(64,80); c.d.polygon([(0,80),(2,70),(14,62),(50,62),(62,70),(64,80)],fill=C['po1'])
    c.r(24,48,40,64,'e2'); c.d.polygon([(25,62),(32,73),(39,62)],fill=C['e2']); c.d.polygon([(16,63),(26,66),(32,73),(38,66),(48,63),(44,60),(32,66),(20,60)],fill=C['po2'])
    face=[(17,30),(18,20),(25,15),(39,15),(46,20),(47,30),(46,42),(42,51),(37,55),(27,55),(22,51),(18,42)]
    fm(c,mk(64,80,lambda d:d.polygon(face,fill=255)),lambda x,y:'e2' if (x>=44 or y>=53 or (x>=42 and (x+y)%2==0)) else 'e1')
    c.d.ellipse((14,31,18,39),fill=C['e2']); c.d.ellipse((46,31,50,39),fill=C['e2'])
    def hm(d): d.ellipse((16,5,48,27),fill=255); d.polygon([(19,32),(20,19),(28,16),(36,16),(44,19),(45,32)],fill=0)
    fm(c,mk(64,80,hm),lambda x,y:'eh2' if (x*2+y*3)%9==0 and y<22 else 'eh')
    for t in range(0,181,18): c.d.ellipse((32+15*math.cos(math.radians(t))-2,15-10*math.sin(math.radians(t))-2,32+15*math.cos(math.radians(t))+2,15-10*math.sin(math.radians(t))+2),fill=C['eh'])
    for t in range(8,180,32): c.p(int(32+12*math.cos(math.radians(t))),int(15-8*math.sin(math.radians(t))),'eh2')
    c.r(23,24,30,24,'eh'); c.r(21,25,30,25,'eh'); c.r(34,24,41,24,'eh'); c.r(34,25,43,25,'eh')
    for x0 in (20,34):
        for y in range(29,37):
            for x in range(x0+1,x0+11): c.p(x,y,'ln')
        c.r(x0+1,28,x0+10,28,'gd'); c.p(x0,29,'lg'); c.p(x0+11,29,'lg')
    c.r(31,29,33,29,'gd'); c.p(31,35,'lg'); c.p(33,35,'lg'); c.r(14,30,19,30,'gd'); c.r(45,30,50,30,'gd')
    for cx in (26,39):
        c.r(cx-3,31,cx+2,31,'lk'); c.r(cx-3,32,cx-2,33,'sw'); c.r(cx+1,32,cx+2,33,'sw'); c.r(cx-1,32,cx,33,'ir'); c.p(cx-1,32,'sw'); c.r(cx-2,34,cx+1,34,'e2')
    for y in range(33,40): c.p(32,y,'e2')
    for x,y in((30,40),(31,41),(33,41),(34,40),(31,42),(32,42),(33,42)): c.p(x,y,'e3')
    c.r(25,44,30,44,'eh'); c.r(34,44,39,44,'eh'); c.r(24,45,29,45,'eh'); c.r(35,45,40,45,'eh'); c.r(28,46,36,46,'ep'); c.r(29,47,35,48,'ep'); c.p(27,46,'e3'); c.p(37,46,'e3')
    fm(c,mk(64,80,lambda d:d.polygon([(18,36),(20,48),(26,55),(38,55),(44,48),(46,36),(44,44),(38,51),(26,51),(20,44)],fill=255)),lambda x,y:'es' if (x*7+y*13)%5<2 else 'e1')
    for x in range(27,38): c.p(x,53,'es') if x%2 else c.p(x,54,'es')
    return c,dict(cabelo=(14,3,36,16),oculos=(19,27,28,11),bigode=(24,43,16,6),barba=(20,48,26,8),porte=(0,62,64,18))
def beach_dusk():
    c=Cv(320,180); sky(c,100,['dk1','dk2','dk3','dk4','dk5']); rnd=random.Random(11); c.d.ellipse((248,14,262,28),fill=C['c1']); c.d.ellipse((251,12,265,26),fill=C['dk1'])
    for col,hmin,hmax,lit in (('dk3',14,36,0),('k0',20,66,1)):
        x=-6
        while x<320:
            w=rnd.randint(8,18); h=rnd.randint(hmin,hmax); c.r(x,100-h,x+w-1,100,col)
            if lit:
                for yy in range(100-h+3,98,4):
                    for xx in range(x+2,x+w-2,3):
                        if rnd.random()<.32: c.r(xx,yy,xx+1,yy+1,rnd.choice(['a1','a2','a1','c1']))
            x+=w+rnd.randint(0,2)
    c.r(188,30,224,100,'k0'); c.r(196,52,205,65,'k0'); c.r(197,53,204,64,'a2'); c.r(200,53,201,64,'k0'); c.r(197,58,204,58,'k0')
    for y in range(40,98,5): c.r(192,y,193,y+1,'a1'); c.r(216,y+2,217,y+3,'a1')
    c.r(0,100,319,128,'n2')
    for y in (104,109,114,119,124):
        for x in range(rnd.randint(0,10),319,14): c.r(x,y,x+6,y,'n3')
    for x in range(120,320,5):
        if rnd.random()<.6:
            for y in range(101,101+rnd.randint(3,14)):
                if (x+y)%2==0: c.p(x,y,'a1')
    c.r(0,128,319,179,'sd1'); c.r(0,128,319,137,'sd2')
    for _ in range(320): c.p(rnd.randint(0,319),rnd.randint(139,179),'sd3')
    for x in range(320):
        y=127+int(1.5*math.sin(x/7)); c.p(x,y,'c1'); c.p(x,y+1,'c1') if x%3 else None
    return c.im
def sunset():
    c=Cv(320,180); sky(c,96,['sn1','sn2','sn3','sn4','sn5','sn6']); B_=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5]; SX,SY=110,92; rnd=random.Random(6)
    for y in range(36,96):
        for x in range(40,181):
            d=(((x-SX)/70)**2+((y-SY)/56)**2)**.5
            if d<1 and (1-d)*16>B_[(y%4)*4+x%4]+5: c.p(x,y,'sn6')
    c.d.ellipse((SX-15,SY-15,SX+15,SY+15),fill=C['sun']); c.d.ellipse((SX-17,SY-17,SX+17,SY+17),outline=C['sn6'])
    for y in range(96,180):
        t=y-96; xs=int(230-t*2.86); c.r(0,y,max(xs,0),y,'se1' if y<118 else 'se2')
        for x in range(SX-int(t*.7)-4,SX+int(t*.7)+5):
            if 0<=x<=xs and (x+y)%2==0 and rnd.random()<.7: c.p(x,y,'sn5' if rnd.random()<.6 else 'sn6')
        if xs<319: c.r(max(xs+1,0),y,319,y,'sa1')
        for x in range(max(xs+1,0),min(320,xs+2+int(t*.18)+4)): c.p(x,y,'sa3')
        if 0<=xs<320: c.p(xs,y,'c1'); c.p(xs+1,y,'c1') if y%2 else None
    for x in range(230,320): c.r(x,92+int(2*math.sin(x/17)),x,96,'sa3')
    for _ in range(260):
        x,y=rnd.randint(190,319),rnd.randint(100,179)
        if x>230-(y-96)*2.86+20: c.p(x,y,'sa2')
    for px,py in((276,96),(300,100)):
        c.r(px,py-34,px+1,py,'k0')
        for dx,dy in((-10,-4),(10,-5),(-7,2),(8,1),(0,-8)): c.d.line((px,py-34,px+dx,py-34+dy+6),fill=C['k0'],width=2)
    return c.im
def golden():
    c=Cv(320,180); sky(c,100,['gs1','gs2','gs3','gs4','gs5']); rnd=random.Random(13); B_=[0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5]
    for y in range(20,100):
        for x in range(190,285):
            d=(((x-237)/47)**2+((y-66)/46)**2)**.5
            if d<1 and (1-d)*16>B_[(y%4)*4+x%4]+6: c.p(x,y,'a2')
    c.d.ellipse((226,56,248,78),fill=C['a2'])
    for cx,cy,w in((40,30,30),(120,18,24),(290,38,26)): c.d.ellipse((cx-w,cy-4,cx+w,cy+4),fill=C['gs3']); c.d.ellipse((cx-w//2,cy-8,cx+w//2,cy),fill=C['gs3'])
    for col,hmin,hmax in (('gb1',10,34),('gb2',14,44)):
        x=-6
        while x<320:
            w=rnd.randint(8,16); h=rnd.randint(hmin,hmax); c.r(x,100-h,x+w-1,100,col)
            for yy in range(100-h+3,98,4):
                for xx in range(x+2,x+w-2,3):
                    if rnd.random()<.2: c.p(xx,yy,'c1')
            x+=w+rnd.randint(0,2)
    c.r(0,100,319,130,'gv1')
    for y in range(100,130,3): c.r(0,y,319,y,'gv2') if (y//3)%2 else None
    for _ in range(90):
        x,y=rnd.randint(205,270),rnd.randint(101,129)
        c.p(x,y,'c1' if rnd.random()<.5 else 'a2')
    c.r(0,130,319,179,'sg1'); c.r(0,130,319,138,'sg3')
    for _ in range(300): c.p(rnd.randint(0,319),rnd.randint(140,179),'sg2')
    for x in range(320): y=129+int(1.5*math.sin(x/8)); c.p(x,y,'c1'); c.p(x,y+1,'c1') if x%3 else None
    c.r(226,150,318,151,'w3'); c.r(226,152,318,155,'w2'); c.r(226,156,318,179,'w1'); c.r(230,156,234,179,'w2'); c.r(310,156,314,179,'w2')
    c.r(44,96,46,150,'w2'); c.r(44,96,44,150,'w3')
    for dx,dy in((-22,10),(24,10),(-16,-6),(18,-8),(0,-14)): c.d.line((45,96,45+dx,96+dy),fill=C['gl'],width=3); c.d.line((45,96,45+dx,96+dy),fill=C['gr'],width=1)
    return c.im
def sh(S,name,frames,ref=None,extra=None):
    w,h=frames[0].size; S[name]=dict(src=save(sheet(frames,w,h),f'assets/sprites/{name}.png'),w=w,h=h,n=len(frames),dy=(ref-h) if ref else 0)
    if extra: S[name].update(extra)
def main():
    B.main(); S=BS.build()
    for k,n in(('him','eu'),('her','karollyne')):
        raw=[back(k,0),back(k,1),back(k,0,1,0),back(k,1,0,1)]
        if k=='him': raw=[B.bulk(r) for r in raw]
        sh(S,n+'_b',[outline(r).im for r in raw],48); sh(S,n+'_bs',[outline(half(r)).im for r in raw],25)
    sh(S,'eu_give',[person('him',0,False,True).im,person('him',1,False,True).im],48); sh(S,'karollyne_rcv',[person('her',0,False,False,True).im,person('her',1,False,False,True).im],48)
    sc={}
    for n,fn in(('her_bust',her_bust),('him_bust',him_bust)):
        c,a=fn(); sh(S,n,[c.im],None,{'a':a}); sc[n]=c
    for n,im in(('beach',beach_dusk()),('sunset',sunset()),('golden',golden()),('frame',BS.select(False))): S[n]=dict(src=save(im,f'assets/scenes/{n}.png'),w=320,h=180,n=1)
    cv=Image.open(os.path.join(R,S['sunset']['src'])).copy()
    for n,(x,y) in(('him_bust',(26,40)),('her_bust',(138,34))):
        o=outline(sc[n]).im; o=o.resize((o.width*2,o.height*2),Image.NEAREST); cv.paste(o,(x,y),o)
    S['capa']=dict(src=save(cv,'assets/scenes/capa.png'),w=320,h=180,n=1)
    p=os.path.join(R,'assets/manifest.js'); M=json.loads(open(p).read()[len('window.MANIFEST='):-1]); M.update(S); open(p,'w').write('window.MANIFEST='+json.dumps(M,indent=1)+';')
    sheetim=Image.new('RGBA',(640,540),(10,14,31,255))
    for i,n in enumerate(('capa','beach','sunset','golden')): sheetim.alpha_composite(Image.open(os.path.join(R,M[n]['src'])).convert('RGBA'),((i%2)*320,(i//2)*180))
    for i,n in enumerate(('her_bust','him_bust')): im=Image.open(os.path.join(R,M[n]['src'])); sheetim.alpha_composite(im.resize((128,160),Image.NEAREST),(20+i*140,360-0))
    fr=lambda n,f=0:Image.open(os.path.join(R,M[n]['src'])).crop((f*M[n]['w'],0,f*M[n]['w']+M[n]['w'],M[n]['h']))
    x=300
    for n in('eu','karollyne','eu_b','karollyne_b'): sheetim.alpha_composite(fr(n),(x,420)); x+=M[n]['w']+6
    sheetim.resize((1280,1080),Image.NEAREST).save(os.path.join(R,'assets/reference/v2_previa.png')); print('ok')
if __name__=='__main__': main()
