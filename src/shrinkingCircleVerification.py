import sys
import cv2
import math
from deepface import DeepFace
from PIL import Image, ImageDraw

img1Path = 'images/bradpittCropped.jpg'
img2Path = 'images/bradpitt_02.jpg'
exportPath = 'images/exported/exportVerification.jpeg'

im = Image.open(img1Path)
w, h = im.size
radius = w/2
centerX = w//2
centerY = h//2

while True:

    radius = math.floor(radius * 0.98)
    print(radius)

    with Image.open(img1Path) as im:

        draw = ImageDraw.Draw(im)
        topLeft = (centerX - radius, centerY - radius)
        bottomRight = (centerX + radius, centerY + radius)
        draw.ellipse([topLeft, bottomRight], fill = (255, 0, 255, 255), outline = None, width = 0)
        im.save(exportPath)
        #if radius <= 300:
        #    break
        result = DeepFace.verify(img1_path = exportPath, img2_path = img2Path, enforce_detection = False)
        print(result['verified'])
        if result['verified'] == True :
            break
        if radius <= 0:
            break
