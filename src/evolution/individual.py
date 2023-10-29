import random
import math
from common import *
from PIL import Image, ImageDraw

class Individual:
    exportPath = 'evolution/individuals/'
    referencePath = 'evolution/reference/bradpittCropped.jpg'
    color = {'r': random.uniform(0,1), 'g': random.uniform(0,1), 'b': random.uniform(0,1)}
    circles = []
    totalArea = 0
    fitness = 0
    id = 0

    def __init__(self):
        self.circles.append(createCircle())

    def fromCopy(self, color, circles):
        self.color = color
        self.circles = circles

    def setFitness(self, fitness):
        self.fitness = fitness

    def mutate(self, mutationRate):
        if random.uniform(0,1) < (mutationRate/2):
            if len(self.circles) > 1 and random.uniform(0,1) < .5:
                self.circles.pop(random.randrange(len(self.circles))) 
            else:
                self.circles.append(createCircle())

        for c in self.circles:
            if random.uniform(0,1) < mutationRate:
                c['x'] = clamp(c['x'] + random.uniform(-0.1, 0.1), 0, 1)
                c['y'] = clamp(c['y'] + random.uniform(-0.1, 0.1), 0, 1)
                c['radius'] = clamp(c['radius'] + random.uniform(-0.1, 0.1), 0, 1)
    
    def crossover(self, individual):
        child = Individual()
        child.circles = []


        if random.uniform(0,1) < 0.5:
            child.color['r'] = self.color['r']
        else:
            child.color['r'] = individual.color['r']

        if random.uniform(0,1) < 0.5:
            child.color['g'] = self.color['g']
        else:
            child.color['g'] = individual.color['g']

        if random.uniform(0,1) < 0.5:
            child.color['b'] = self.color['b']
        else:
            child.color['b'] = individual.color['b']


        for i in range(len(self.circles)):
            if random.uniform(0,1) < 0.5:
                child.circles.append(self.circles[i])
            elif i < len(individual.circles):
                child.circles.append(individual.circles[i])

        return child

    def exportImage(self):
        circleAreaSum = 0
        imageArea = 0

        with Image.open(self.referencePath) as im:
            w, h = im.size
            imageArea = w * h
            draw = ImageDraw.Draw(im)

            for circle in self.circles:
                
                x = math.floor(circle['x'] * w)
                y = math.floor(circle['y'] * h)
                radius = math.floor(circle['radius'] * w * .2)

                area = math.pi * ((radius*w) ** 2) 
                circleAreaSum += area
                
                topLeft = (x - radius, y - radius)
                bottomRight = (x + radius, y + radius)
                draw.ellipse([topLeft, bottomRight], fill = (math.floor(255*self.color['r']), math.floor(255*self.color['g']), math.floor(255*self.color['b']), 255), outline = None, width = 0)
            path = self.getImagePath()
            im.save(path)

        self.totalArea = clamp(circleAreaSum / imageArea, 0, 1)

    def getImagePath(self):
        return self.exportPath + str(self.id) + '.jpeg'

    def getCopy(self):
        copiedIndividual = Individual()
        copiedIndividual.fromCopy(self.color.copy(), self.circles.copy())
        return copiedIndividual
