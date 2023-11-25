import sys
import cv2
import math
from deepface import DeepFace
from PIL import Image, ImageDraw

imgPath = 'images/bradpittCropped.jpg'
exportPath = 'images/exported/exportExtraction.jpeg'

im = Image.open(imgPath)
w, h = im.size
radius = w
centerX = w//2
centerY = h//2

while True:

    radius = math.floor(radius * 0.98)
    print(radius)

    with Image.open(imgPath) as im:

        draw = ImageDraw.Draw(im)
        topLeft = (centerX - radius, centerY - radius)
        bottomRight = (centerX + radius, centerY + radius)
        draw.ellipse([topLeft, bottomRight], fill = (255, 0, 255, 255), outline = None, width = 0)
        im.save(exportPath)
        #if radius <= 300:
        #    break
        result = DeepFace.extract_faces(exportPath, align=False, enforce_detection = False)
        print(result[0]['confidence'])
        if result[0]['confidence'] > 5 :
            break
        if radius <= 0:
            break
