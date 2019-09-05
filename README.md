# Image-to-Text-Converter
This repository contains some python programs which convert textual data into image format and then that image is converted back to text,Basically its the new way of encrypting data.

## ASCII Converter
### ASCII text to image converter
The pyhton program in this folder can convert the txt file,whose textual data contain ascii characters into a .bmp file.
you just have to given the path of your .txt file when you run the program.

### ASCII image to text converter 
The pyhton program in this folder is reverse engineered program for the ascii text to image converter.

## UNICODE Converter
### UNICODE text to image converter
The pyhton program in this folder can convert the txt file,whose textual data contain unicode characters into a .bmp file.
you just have to given the path of your .txt file when you run the program.
Now , why we need this if we have already ascii converter?
The answer is ascii converter can convert data only having ascii characters and unicode convert every character .

### UNICODE image to text converter 
The pyhton program in this folder is reverse engineered program for the UNICODE text to image converter.

## MAJOR DIFFERENCES
1. UNICODE text to image converter, can convert the file with any form of language.
2. ASCII converter generate smaller size image than unicode because in ascii,3 character represent the one pixel value and in unicode, 1character represent the one pixel . so to convert the entire textual data we require less pixel in ascii converter.

## RESEARCH CONVERTER
Most of the time .txt files contains only one language like english and some special characters etc.so instead of using entire unicode.we can create a dictionary for these symbols and use them directly for specific language. for example, if we have to make dictionary for english than there are 52 language characters (both lower and uppercase letter) and 10 integer symbols and 30-40 special characters.now with the smaller dictionary than the entire unicode we can make our own system to generate pixels from characters.so,in the research converter i made my own system with dictionary containing only 26 uppercase english characters(we can expand dictionary).Now, In this sytem with 6 characters (which is greater than ascii which convert 3 character into 1 pixel and unicode which convert 1 character into 1 pixel) i can make 1 pixel. now Let say the characters are("IJBLGH" as i have taken only 26 english charaters so i cant take space or integer or special but we can do so just by adding them into dictionary and changing the divisionfactor which is equal to length of dictionary,we will discuss it) now to represent R,G,B value of pixel which range from(0-255).i pick characters in pair of two and there values in dictionary(ike i have given values like for A=0,B=1 ,C=2 and Z=25)
ok from example 'IJBLGH' i pick IJ now there values from dictinary are(8,9) so we represent the value of R as 8*(divfact)+9 (in my case div fact is 26).so acc to this 'IJBLGH' can we represented as pixel value ( (8 * 26)+9  , (1 * 26)+11  , (6*26)+7 ).but it has some issues like first character in pair cannot exceed (I=9) otherwise .rgb value will exceed 255.so it is just to represnt that  we can create a system using our own dictionary set.thatswhy this folder is named as research converter,if you want to work on that you can take the material as refrence. 
