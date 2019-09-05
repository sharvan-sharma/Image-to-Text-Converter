#import
import math
import time
import os
from PIL import Image
#conversion of unicode text into image
def pixeltuple(c):
    n = ord(c);rgb=()
    R=(n//256)//256
    G=(n//256)%256
    B=n%256
    rgb=rgb+(int(R),int(G),int(B))
    return rgb
def imghw(fsize):
    hwtuple=()
    #if square root of file size is smaller than  6000 than we will take width as square root of file size ,else width=2000
    if (fsize**(0.5)) < 2000:
        width = int(fsize**(0.5))+1
    else:
        width = 2000
    #code to generate the height from width
    height = math.ceil(fsize/width)
    hwtuple = hwtuple+(int(width),int(height),)
    return hwtuple
def imggen(filename,imname,start,fsize):
    #reading the f object with the buffer size (in bytes) equal to file size if file is less than 50 mb,else buffer size = 50 mb
    if fsize < 50111111 :
        f = open(filename,"r",fsize)
    else:
        f = open(filename,"r",50111111)
    #f is reading 16 mb of data in buffer
    #getting the height and width of image
    hwtuple =  imghw(fsize)
    img = Image.new('RGB',hwtuple, color=(0, 0, 0))
    pixv=img.load()
    flag=""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            c = f.read(1)
            if c == "":
                flag="break"
                break      
            tpl = pixeltuple(c)
            pixv[j,i] = tpl
        if flag=="break":
           break
    f.close()
    img.show()
    img.save(imname)
    img.close()
#def file size function and filename function
def filesize(path):
    try: 
        b = os.path.getsize(path)
        return b
    except OSError :
        print("path does not exist")
        sys.exit()
def filename(path):
    try: 
        head,tail = os.path.split(path)
        return tail
    except OSError :
        print("path does not exist")
        sys.exit()
#connverting and generating a new image name
def ip(name):
    k=0
    imname=''
    dtarr=['txt']# storing the datatypes
    while(k<len(name)):
        if name[k]=='.' :
            if name[k+1:len(name)] in dtarr:
                imname=name[0:k]+'.bmp'
                break
        k=k+1
    return imname
#input file path
path = input()
name = filename(path)
fsize = filesize(path)
if fsize>5111111:
    imname = ip(name)
    a = imggen(name,imname,start,fsize)
else:
    print("This program works only if file size is less than 50 mb,otherwise wait for updation by developer")
    sys.exit()
