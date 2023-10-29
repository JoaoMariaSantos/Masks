import math
from deepface import DeepFace
from PIL import Image, ImageDraw

def evaluate(individual):
    result = DeepFace.extract_faces(individual.getImagePath(), align=False, enforce_detection = False)
    confidence = result[0]['confidence'] / 10
    area = individual.totalArea

    #fitness = (10 - confidence) / 10
    fitness = 1 - confidence * .25 - area
    return fitness