from PIL import Image
import cv2

imagePath = 'images/hatim.jpg'
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

background_image.save('result/result.' + background_image.format)
background_image.show()
