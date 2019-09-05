#timing 137s highly efficient when most of the pixel have same value
#import
import time
from PIL import Image
#code

#function converter
def converter(value,d):
    #variables
    i=0
    q=()
    s=''
    dic={1:'A',2:'B',3:'C',4:'D',
         5:'E',6:'F',7:'G',8:'H',
         9:'I',10:'J',11:'K',12:'L',
         13:'M',14:'N',15:'O',16:'P',
         17:'Q',18:'R',19:'S',20:'T',
         21:'U',22:'V',23:'W',24:'X',
         25:'Y',26:'Z'
          }
    #code
    while(i<3):
        quo=(value[i]//26)
        rem=(value[i]%26)
        #because quo become zero and we want to store value at 0 as 'A'
        s=s+dic[quo+1]+dic[rem+1]
        i=i+1
    s=s+str(d)
    return s    
#direct code
#input
name=input()
#starting
start=time.time()
#code continue
img  = Image.open(name)
k=0
txname=''
dtarr=['jpg','png','jpeg']# storing the datatypes
while(k<len(name)):
    if name[k]=='.' :
        if name[k+1:len(name)] in dtarr:
            txname=name[0:k]+'.txt'
            break
    k=k+1
#getting height width 
width=img.size[0]
height=img.size[1]
#variables
i=0
j=0
m=()
value=()
f=open(txname,"w")
t=(width,height)
f.write(str(t))
f.write("\n")
while(i<height):
    while(j<width):
        coordinate=(j,i)
        if j==0 and i==0:
            m=img.getpixel(coordinate)
            value=m
            d=1
        elif j!=(width-1) or i!=(height-1):
            m=img.getpixel(coordinate)
            if m==value:
                d=d+1
            else:
                #adding pixel code
                q=converter(value,d)
                f.write(q)
                #changing the value of pixel
                value=m
                d=1
        elif j==(width-1) and i==(height-1):
            m=img.getpixel(coordinate)
            if m==value:
                #incrementing d because last is also a match
                d=d+1
                #converting andadding a value
                q=converter(value,d)
                f.write(q)
            else:
                #storing the previous matched value
                q=converter(value,d)
                f.write(q)
                #changing the value of pixel
                value=m
                d=1
                #storing the last different value
                q=converter(value,d)
                f.write(q)       
        j=j+1
    j=0
    i=i+1
f.close()
#ending
end=time.time()
print(end-start)
