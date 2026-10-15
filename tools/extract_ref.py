"""Reconstrói sprites, retratos, expressões, objetos e capa a partir da referência oficial (assets/reference/referencia_oficial.png).
Cada recorte tem o fundo removido, é reduzido, quantizado em poucas cores e recebe contorno de 1 px: resultado em pixel art nítida."""
import numpy as np, os
from PIL import Image
from collections import deque
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF=Image.open(os.path.join(R,'assets/reference/referencia_oficial.png')).convert('RGB')
def remove_bg(im,tol=26):
    a=np.array(im).astype(int); h,w,_=a.shape
    edge=np.concatenate([a[0],a[-1],a[:,0],a[:,-1]]); bg=np.median(edge,axis=0)
    d=np.sqrt(((a-bg)**2).sum(2)); near=d<tol; seen=np.zeros((h,w),bool); q=deque()
    for x in range(w):
        for y in (0,h-1):
            if near[y,x] and not seen[y,x]: seen[y,x]=True; q.append((y,x))
    for y in range(h):
        for x in (0,w-1):
            if near[y,x] and not seen[y,x]: seen[y,x]=True; q.append((y,x))
    while q:
        y,x=q.popleft()
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
            Y,X=y+dy,x+dx
            if 0<=Y<h and 0<=X<w and near[Y,X] and not seen[Y,X]: seen[Y,X]=True; q.append((Y,X))
    al=(~seen).astype(np.uint8)*255; out=np.dstack([a.astype(np.uint8),al]); return Image.fromarray(out,'RGBA')
def clean(im,min_area=12):  # mantém só o maior componente (remove brilhos e sobras)
    a=np.array(im); m=a[:,:,3]>0; h,w=m.shape; lab=np.zeros((h,w),int); n=0; sizes={}
    for y in range(h):
        for x in range(w):
            if m[y,x] and not lab[y,x]:
                n+=1; q=deque([(y,x)]); lab[y,x]=n; c=0
                while q:
                    cy,cx=q.popleft(); c+=1
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        Y,X=cy+dy,cx+dx
                        if 0<=Y<h and 0<=X<w and m[Y,X] and not lab[Y,X]: lab[Y,X]=n; q.append((Y,X))
                sizes[n]=c
    if not sizes: return im
    keep=[k for k,v in sizes.items() if v>=max(min_area,max(sizes.values())*.04)]
    a[:,:,3]=np.where(np.isin(lab,keep),255,0); return Image.fromarray(a,'RGBA')
def pix(im,height=None,scale=None,colors=28,outline=True):
    bb=im.getbbox(); im=im.crop(bb); 
    if scale is None: scale=height/im.height
    w,h=max(1,round(im.width*scale)),max(1,round(im.height*scale))
    pm=np.array(im).astype(float); pm[:,:,:3]*=pm[:,:,3:4]/255; small=Image.fromarray(pm.astype(np.uint8),'RGBA').resize((w,h),Image.BOX)
    s=np.array(small).astype(float); al=s[:,:,3]; rgb=np.where(al[:,:,None]>0,s[:,:,:3]/np.maximum(al[:,:,None],1)*255,0).clip(0,255).astype(np.uint8)
    mask=al>110; q=Image.fromarray(rgb,'RGB').quantize(colors=colors,method=Image.MEDIANCUT,dither=Image.NONE).convert('RGB')
    out=np.dstack([np.array(q),(mask*255).astype(np.uint8)]); o=Image.fromarray(out,'RGBA')
    return add_outline(o) if outline else o
def add_outline(o):
    if True:
        a=np.array(o); pad=np.zeros((a.shape[0]+2,a.shape[1]+2,4),np.uint8); pad[1:-1,1:-1]=a; m=pad[:,:,3]>0; new=m.copy()
        new[1:,:]|=m[:-1,:]; new[:-1,:]|=m[1:,:]; new[:,1:]|=m[:,:-1]; new[:,:-1]|=m[:,1:]; ring=new&~m; pad[ring]=(10,6,22,255); return Image.fromarray(pad,'RGBA')
def sprite(box,height,tol=26):
    return pix(clean(remove_bg(REF.crop(box),tol)),height=height)
def flip(i): return i.transpose(Image.FLIP_LEFT_RIGHT)
