"""
@Author : AJDAINI Hatim
@GitHub : https://github.com/Hajdaini
"""

from PIL import Image
import cv2
import sys

if len(sys.argv) == 2:
    imagePath = sys.argv[1]
else:
    print('Error : you have to run the program like this :\npyhton3 thug_life_maker.py our_full_path_image.jpg')
    exit(-1)

maskPath = "images/mask.png"
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread(imagePath)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray_image, 1.15)
background_image = Image.open(imagePath)

for (x, y, width, height) in faces:
    cv2.rectangle(image, (x,y), (x+width, y+height), (0, 0, 255), 2)
    mask = Image.open(maskPath)
    mask = mask.resize((width, height), Image.ANTIALIAS)# ANTIALIAS to make image smooth
    offset = (x, y)
    background_image.paste(mask, offset, mask=mask)# mask= keep transparency
    
try:
    background_image.save('result/result.{}'.format(background_image.format))
    print('successfully saved in result/result.{}'.format(background_image.format))
except:
    print('Failed to saved the image')
    exit(-1)

try:
    background_image.show()
except:
    print('make sure that you have an image viewer installed in your system')
    exit(-1)
