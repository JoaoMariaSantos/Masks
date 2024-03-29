import math
from deepface import DeepFace

def evaluate(individual, facePath):

    #result = DeepFace.extract_faces(individual.getImagePath(), align=False, enforce_detection = False)
    #confidence = result[0]['confidence'] / 10

    result = DeepFace.verify(img1_path = individual.getImagePath(), img2_path = facePath, enforce_detection = False)
    confidence = int(result['verified']) #bool verified or not
    distance = float(result['distance']) #float distance between images from 0 to 1
    #confidence = result['distance'] #distance between faces

    area = float(individual.info['area'])

    #print()
    #print('c: ' + str(confidence))
    #print('d: ' + str(distance)) 

    #fitness = 1 - ((1-distance) * .7) - (area * .3)
    fitness = distance

    individual.setInfo(fitness, distance, area)