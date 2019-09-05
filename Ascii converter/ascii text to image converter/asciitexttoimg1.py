#import
import math
import os
from PIL import Image
#conversion of unicode text into image
def pixeltuple(c):
    R = ord(c[0]);G = ord(c[1]);B = ord(c[2]);rgb=()
    rgb=rgb+(int(R),int(G),int(B))
    return rgb
#function to generate height and width
def imghw(fsize):
    hwtuple=()
    #if square root of file size is smaller than  6000 than we will take width as square root of file size ,else width=2000
    if (fsize**(0.5)) < 2000:
        width = int(fsize**(0.5))+1
    else:
        width = 2000
    #code to generate the height from width
    height = math.ceil(fsize/(width*3))
    #returning tuple containing height and width
    hwtuple = hwtuple+(int(width),int(height),)
    return hwtuple
#function to generate the image
def imggen(filename,imname,fsize):
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
    flag="";st="";c1=""; c2="";c3=""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            c1 = f.read(1)
            c2 = f.read(1)
            c3 = f.read(1)
            #condition to check if last read values are "" ,then we have to add spaces according to it.
            if c3 == "":
                st = c1 + c2 + ' '
                flag="break"
                tpl = pixeltuple(st)
                pixv[j,i] = tpl
                break
            if c2 == "":
                st = c1 + ' ' + ' '
                flag="break"
                tpl = pixeltuple(st)
                pixv[j,i] = tpl
                break
            if c1 == "":
                flag="break"
                break
            st = c1 + c2 + c3
            tpl = pixeltuple(st)
            pixv[j,i] = tpl
            st="";c1=""; c2="";c3=""
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
#entire functional code
print('Enter the path of .txt file')
#input file path
path = input()
#caling filename function to get the file name
name = filename(path)
#caling filesize function to get the file size
fsize = filesize(path)
#calling ip function to generate image name for the image file that we create
imname = ip(name)
#calling the umggen function which produce the image from the given ascii text
#parameters of imggen functions are
""" name : stores the filename
imname:stores the name for new image
fsize:store te size of image"""
if fsize < 5111111 :
    a = imggen(name,imname,fsize)
else:
    print("file is too large this program is able to take only file upto 50 mb")
    sys.exit()
