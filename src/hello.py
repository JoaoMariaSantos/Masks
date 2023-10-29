import sys
import cv2
from deepface import DeepFace
from PIL import Image, ImageDraw

print("")
print("")
print("")

img_path = 'images/bradpitt.jpg'

print(DeepFace.extract_faces('images/bradpitt.jpg', align=False, enforce_detection = False))

paintedImgFolderPath = 'images/painted/bradpitt/'
paintedImgPaths = []
paintedImgFaces = []

for i in range(1,7):
    paintedImgPaths.append(paintedImgFolderPath + 'bradpitt_0' + str(i) + '.jpg')

for p in paintedImgPaths:
    paintedImgFaces.append(DeepFace.extract_faces(p, align=False, enforce_detection = False))

#result = DeepFace.verify(img1_path = img1_path, img2_path = img2_path)
#print(result)

#img1 = DeepFace.detectFace(img2_path)

#extractedFaceInfo = DeepFace.extract_faces(img2_path, align=False, grayscale=True)
#analysisInfo = DeepFace.analyze(img2_path)

print(paintedImgFaces[5])

while True:
    for i in range(len(paintedImgFaces)):
        cv2.imshow(paintedImgPaths[i], paintedImgFaces[i][0]["face"])
    #cv2.imshow("Image", extractedFaceInfo[0]["face"])
    cv2.waitKey(0)
    sys.exit()

cv2.destroyAllWindows()