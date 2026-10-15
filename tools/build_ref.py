"""Integra a referência oficial ao jogo: sprites, retratos, expressões, objetos e capa. Uso: python3 tools/build_ref.py"""
import sys, os, json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from extract_ref import *
import build_v2 as V2
from PIL import ImageDraw
HER=[(992,98,1062,254),(1085,98,1140,254),(1170,98,1226,254),(1243,98,1312,254)]
HIM=[(1002,445,1062,600),(1085,445,1135,600),(1165,445,1220,600),(1245,445,1308,600)]
def cut(box,h=None,tol=8,**kw):
    raw=clean(remove_bg(REF.crop(box),tol),min_area=3)
    return pix(raw,height=h,**kw) if h else pix(raw,**kw)
def breath(im):
    w,h=im.size; sp=int(h*.42); o=Image.new('RGBA',(w,h),(0,0,0,0)); o.alpha_composite(im.crop((0,sp,w,h)),(0,sp)); o.alpha_composite(im.crop((0,0,w,sp+1)),(0,1)); return o
def place(im,y,fl=False,H=None):
    w,h=im.size; H=H or h+2; o=Image.new('RGBA',(w,H),(0,0,0,0)); o.alpha_composite(flip(im) if fl else im,(0,y)); return o
def edge(im,y,right=True):
    a=np.array(im)[:,:,3]; xs=np.where(a[y]>0)[0]; return int(xs.max() if right else xs.min())
def arm(raw,right,face_y,length,col_sl,col_sk):
    w,h=raw.size; pad=Image.new('RGBA',(w+length+6,h),(0,0,0,0)); ox=0 if right else length+6; pad.alpha_composite(raw,(ox,0)); d=ImageDraw.Draw(pad)
    y=int(h*face_y); xe=ox+edge(raw,y+2,right)
    if right: d.rectangle((xe-3,y+2,xe+length,y+4),fill=col_sl); d.rectangle((xe+length,y+1,xe+length+3,y+5),fill=col_sk); hx=xe+length+2
    else: d.rectangle((xe-length,y+2,xe+3,y+4),fill=col_sl); d.rectangle((xe-length-3,y+1,xe-length,y+5),fill=col_sk); hx=xe-length-2
    return add_outline(pad),(hx+1,y+3)
def portrait(box,scale,colors=48):
    im=REF.crop(box); w,h=int(im.width*scale),int(im.height*scale); q=im.resize((w,h),Image.BOX).quantize(colors=colors,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGBA')
    ImageDraw.Draw(q).rectangle((0,0,w-1,h-1),outline=(240,226,192,255)); return q
def faces(y0,n=5):
    xs=[1005,1071,1136,1198,1260]; out=[]
    for x in xs:
        im=REF.crop((x,y0,x+62,y0+66)).resize((40,42),Image.BOX).quantize(colors=28,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGBA'); out.append(im)
    return out
def keyframes(tw):
    a=np.array(tw); lum=a[:,:,:3].mean(2); h,w=lum.shape; pts=[(x,y) for y in range(int(h*.45),int(h*.85)) for x in range(2,w-3) if lum[y,x]>150 and a[y,x,3]>0]
    out=[tw]; 
    for k in range(5):
        x,y=pts[(k*len(pts))//5+len(pts)//10]; f=tw.copy(); d=ImageDraw.Draw(f); d.rectangle((x,y,x+1,y+1),fill=(242,169,59,255)); d.point((x,y+2),fill=(120,70,30,255)); d.point((x+1,y+2),fill=(120,70,30,255)); out.append(f)
    return out
def main():
    V2.main(); S={}
    for nm,boxes,h,sl,sk in (('karollyne',HER,48,(30,26,34,255),(226,160,130,255)),('eu',HIM,50,(32,26,28,255),(201,130,92,255))):
        views=[cut(b,h) for b in boxes]; f=views[0]
        V2.sh(S,nm,[f,breath(f),f],48)
        bk=views[3]; V2.sh(S,nm+'_b',[place(bk,1),place(breath(bk),1),place(bk,0),place(bk,2,True)],48)
        sm=cut(boxes[3],h//2); V2.sh(S,nm+'_bs',[place(sm,1),place(breath(sm),1),place(sm,0),place(sm,2,True)],25)
        sd=views[1] if nm=='eu' else views[2]; V2.sh(S,nm+'_side',[sd,breath(sd)],48)
        raw=cut(boxes[1] if nm=='eu' else boxes[2],h,outline=False)
        if nm=='eu':
            g,hand=arm(raw,True,.40,12,sl,sk); V2.sh(S,'eu_give',[g,breath(g)],48,{'tip':[hand[0]-6,hand[1]-13]})
            sdw=sd; ys=int(sd.height*.58); xe=edge(sd,ys,True); S['eu_side']['tip']=[xe-9,ys-8]
        else:
            g,hand=arm(raw,False,.40,5,sl,sk); V2.sh(S,'karollyne_rcv',[g,breath(g)],48)
    for nm,box,an in (('her_bust',(800,108,985,388),dict(cabelo=(30,6,60,30),olhos=(37,55,48,16),sorriso=(48,78,26,14),pele=(33,67,54,13),mechas=(0,42,29,48))),
                      ('him_bust',(800,452,990,744),dict(cabelo=(15,9,72,42),oculos=(24,59,63,20),bigode=(47,83,30,10),barba=(41,90,42,17),porte=(0,114,114,54)))):
        p=portrait(box,.6); V2.sh(S,nm,[p],None,{'a':an})
    V2.sh(S,'face_k',faces(321),None); V2.sh(S,'face_e',faces(669),None)
    def prop(name,box,sc=.5,tol=8,frames=None):
        im=pix(clean(remove_bg(REF.crop(box),tol),min_area=3),scale=sc); V2.sh(S,name,frames(im) if frames else [im],None)
    prop('typewriter',(1258,820,1352,864),frames=keyframes); prop('lamp',(1446,783,1494,852)); prop('cat',(1438,858,1494,918)); prop('mug',(1341,866,1394,918)); prop('plant',(1395,856,1438,918))
    prop('monitor',(1358,793,1444,854),frames=lambda i:[i,i]); prop('books',(1256,868,1332,918))
    cv=REF.crop((0,0,768,1024)).resize((384,512),Image.BOX).quantize(colors=64,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGB'); cv.save(os.path.join(R,'assets/scenes/capa.png'))
    S['capa']=dict(src='assets/scenes/capa.png',w=384,h=512,n=1)
    p=os.path.join(R,'assets/manifest.js'); M=json.loads(open(p).read()[len('window.MANIFEST='):-1]); M.update(S); open(p,'w').write('window.MANIFEST='+json.dumps(M,indent=1)+';')
    # folha de contato para conferência
    sheetim=Image.new('RGBA',(480,330),(40,40,70,255)); fr=lambda n,f=0:Image.open(os.path.join(R,M[n]['src'])).convert('RGBA').crop((f*M[n]['w'],0,f*M[n]['w']+M[n]['w'],M[n]['h']))
    x=2
    for n in('karollyne','eu','karollyne_b','eu_b','karollyne_side','eu_side','eu_give','karollyne_rcv','karollyne_bs','eu_bs'): im=fr(n); sheetim.alpha_composite(im,(x,2)); x+=im.width+3
    x=2
    for n in('typewriter','lamp','cat','mug','plant','monitor','books'): im=fr(n,1 if n=='typewriter' else 0); sheetim.alpha_composite(im,(x,66)); x+=im.width+4
    x=2
    for i in range(5): sheetim.alpha_composite(fr('face_k',i),(x,110)); sheetim.alpha_composite(fr('face_e',i),(x,156)); x+=44
    sheetim.alpha_composite(fr('her_bust'),(240,110)); sheetim.alpha_composite(fr('him_bust'),(358,110))
    sheetim.resize((1440,990),Image.NEAREST).save(os.path.join(R,'assets/reference/ref_sprites_contato.png')); print('ok')
if __name__=='__main__': main()
