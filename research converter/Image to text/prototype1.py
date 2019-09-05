#import
import time
from PIL import Image
#code
name=input()
#starting time
start=time.time()
#code continues
img  = Image.open(name)
k=0
txname=''
while(k<len(name)):
    if name[k]=='.':
        txname=name[0:k]+'.txt'
    k=k+1
#img.rotate(180)
width=img.size[0]
height=img.size[1]
i=0
j=0
m=()
s=''
while(i<height):
    while(j<width):
        coordinate=(j,i)
        m=img.getpixel(coordinate)
        s=s+str(m[0])+str(m[1])+str(m[2])
        j=j+1
    if i==0:
        f=open(txname,"w")
        f.write(s)
        f.close()
    else:
        f=open(txname,"a")
        f.write(s)
        f.close()
    j=0
    m=()
    s=''
    i=i+1
#ending
end=time.time()
print(end-start)

