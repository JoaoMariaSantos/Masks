import random
import os
import glob
from pathlib import Path

faceFileName = ''

def createSticker():
    return {'x' : random.uniform(0, 1), 
            'y' : random.uniform(0, 1), 
            'radius' : random.uniform(0,.2),
            'rotation' : random.uniform(0, 1),
            'id' : random.uniform(0, 1)}

def clamp(x, min, max):
    if x > max:
        return max
    if x < min:
        return min
    return x

def setFaceFilename(name):
    print(name)
    global faceFileName
    faceFileName = name

def getFacePath():
    print("GET FACE PATH")
    p = str(Path(__file__).parents[1]) + "/uploads/" + faceFileName
    print(p)
    return p

def getStickersDirPath():
    p = str(Path(__file__).parents[1]) + "/emojis/png"
    return p
