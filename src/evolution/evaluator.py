import math
from deepface import DeepFace
from PIL import Image, ImageDraw

referencePaths = ['images/bradpitt_02.jpg', 'images/bradpitt_03.jpg', 'images/bradpitt_04.jpg']

def evaluate(individual, pathValue):
    pathIndex = math.floor(pathValue * len(referencePaths))

    #result = DeepFace.extract_faces(individual.getImagePath(), align=False, enforce_detection = False)
    #confidence = result[0]['confidence'] / 10

    result = DeepFace.verify(img1_path = individual.getImagePath(), img2_path = referencePaths[pathIndex], enforce_detection = False)
    confidence = int(result['verified']) #bool verified or not
    distance = float(result['distance']) #float distance between images from 0 to 1
    #confidence = result['distance'] #distance between faces

    area = individual.totalArea

    #print()
    #print('c: ' + str(confidence))
    #print('d: ' + str(distance)) 

    fitness = 1 - ((1-distance) * .75) - (area * 10)

    individual.exportInfo(fitness, distance, area)
    individual.setFitness(fitness)