#import
#import
import time
from PIL import Image
#dictionary
dictn={
         'A':1,'B':2,'C':3,'D':4,
         'E':5,'F':6,'G':7,'H':8,
         'I':9,'J':10,'K':11,'L':12,
         'M':13,'N':14,'O':15,'P':16,
         'Q':17,'R':18,'S':19,'T':20,
         'U':21,'V':22,'W':23,'X':24,
         'Y':25,'Z':26,27:' ',28:',',
         29:'.'
             }
number=['0','1','2','3','4','5','6','7','8','9']
#pexel generation from string
def pexelgen(st):
    i=0
    t=()
    while(i<3):
        mul=dictn[st[2*(i)]]
        ad=dictn[st[(2*(i)+1)]]
        #we use mu;-1 and ad-1 instead of mul,ad because we stored earlier A at the zeo but in dict A =1
        pex=(29*(mul-1))+(ad-1)
        t=t+(pex,)
        pex=0
        i=i+1
    return t
#code for getting height and width
def hwfind(wh):
    i=0
    v=''
    width=''
    height=''
    tuplee=()
    number=['0','1','2','3','4','5','6','7','8','9']
    while(i<len(wh)):
        if wh[i] in number:
            v=v+wh[i]
        elif wh[i]==',':
            width=v
            v=''
        elif wh[i]==')':
            height=v
            v=''
            break
        i=i+1
    tuplee=tuplee+(int(width),int(height),)
    return tuplee
#function which enerate pex value and number of pixels
def pexnofpex(last,f):
    #take cursor to the last position
    f.seek(last,0)
    c=f.read(1)#read the first value after last
    f.seek(last,0)#again set to last
    if (c!=''):
        pexel=f.read(6)#reading first six values for pixel generation
        t=pexelgen(pexel)#generating pixel tuple
        nofp=''# number of pixels
        c2=f.read(1)
        while((c2)!=''):
            if c2 in number:
                nofp=nofp+c2
            else:
                c2=''
                break
            c2=f.read(1)
        last=f.tell()-1#storing the last index
        return t,int(nofp),last
    else:
        return 0
#main function which edit pixels
def imggen(filename,imname,start):
    #code for getting height and width
    f=open(filename,"r")
    wh=f.readline()
    tuplee=hwfind(wh)
    last=f.tell()
    img = Image.new('RGB',tuplee, color=(0, 0, 0))
    pixv=img.load()
    flag=''
    tpl=()
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            if i==0 and j==0:
               t=pexnofpex(last,f)
               last=t[2]
               nop=t[1]
               tpl=t[0]
            else:
                if nop ==0 and flag!='filecomplete':
                   t=pexnofpex(last,f)
                   if t==0:
                       flag='filecomplete'
                   else:
                       last=t[2]
                       nop=t[1]
                       tpl=t[0]
            pixv[j,i]=tpl
            nop=nop-1
    f.close()
    img.show()
    img.save(imname)
    img.close()
#input
name=input()
#code continue
def ip(name):
    k=0
    imname=''
    dtarr=['txt']# storing the datatypes
    while(k<len(name)):
        if name[k]=='.' :
            if name[k+1:len(name)] in dtarr:
                imname=name[0:k]+'.jpg'
                break
        k=k+1
    return imname
imname=ip(name)
start=time.time()
a=imggen(name,imname,start)



