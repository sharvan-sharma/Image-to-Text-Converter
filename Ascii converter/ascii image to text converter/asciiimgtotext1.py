#import
import math
import os
from PIL import Image
#reverse engineer
#conversion of image pixel into txt
def pixelstring(p):
    value = chr(p[0])+chr(p[1])+chr(p[2])
    return value
#filename function
def filename(path):
    try: 
        head,tail = os.path.split(path)
        return tail
    except OSError :
        print("path does not exist")
        sys.exit()
#txtgen function
def txtgen(path,txtname):
    #creating file with .txt file wxtension
    f=open(txtname,"w")
    #opening imag efile with path as parameter 'path'
    img  = Image.open(path)
    l = 2000
    flag = "" ; s=''
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            coordinate = (j,i)
            p = img.getpixel(coordinate)
            if p != (0,0,0):
                c = pixelstring(p)
                s = s + c
                l = l - 1
                if l==0:
                    f.write(s)
                    s = ''
                    l = 2000
            else:
                f.write(s)
                flag = "break"
                break
        if flag == "break":
            break
    f.close()           
#converting and generating a text file
def ip(name):
    k=0
    imname=''
    dtarr=['jpg','jpeg','png','bmp']#jpg storing the datatypes
    while(k<len(name)):
        if name[k]=='.' :
            if name[k+1:len(name)] in dtarr:
                imname=name[0:k]+'.txt'
                break
        k=k+1
    return imname
#input file path
print('enter the path of image file')
path = input()
#getting the filename
name = filename(path)
#removing the jpg extension and adding .txt for new name of txt file
txtname = ip(name)
#calling txtgen function for enerating text file
#parameters of text gen is path for image and txtname for the name of new txt file
a = txtgen(path,txtname)
