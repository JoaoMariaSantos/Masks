import random
import math
import os
from common import *
from PIL import Image, ImageDraw
from copy import deepcopy

class Individual:
    exportPath = 'evolution/individuals/'
    referencePath = 'evolution/reference/bradpittCropped.jpg'
    color = (0, 255, 0)
    circles = []
    fitness = 0
    id = 0
    totalArea = 0

    def __init__(self):
        self.circles.append(createCircle())

    def fromCopy(self, color, circles):
        self.color = color
        self.circles = circles

    def setFitness(self, fitness):
        self.fitness = fitness

    def exportInfo(self, fitness, distance, area):
        lines = ['fitness: ' + str(fitness), 
                 'distance: ' + str(distance),
                 'area: ' + str(area)]
        
        with open(self.getTextPath(), 'w') as f:
            f.write('\n'.join(lines))

    def mutate(self, mutationRate):
        """ for i in self.color:
            i = clamp(i + random.uniform(-0.1, 0.1), 0, 1) """

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

        """ childColor = []

        for i in range(len(self.color)):
            if random.uniform(0,1) < 0.5:
                childColor.append(self.color[i])
            else:
                childColor.append(individual.color[i])

        child.color = tuple(childColor) """

        for i in range(len(self.circles)):
            if random.uniform(0,1) < 0.5:
                child.circles.append(self.circles[i])
            elif i < len(individual.circles):
                child.circles.append(individual.circles[i])

        return child

    def exportImage(self):
        with Image.open(self.referencePath) as im:
            w, h = im.size
            draw = ImageDraw.Draw(im)

            for circle in self.circles:
                
                x = math.floor(circle['x'] * w)
                y = math.floor(circle['y'] * h)
                radius = math.floor(circle['radius'] * w * .2)
                
                topLeft = (x - radius, y - radius)
                bottomRight = (x + radius, y + radius)
                #draw.ellipse([topLeft, bottomRight], fill = (math.floor(255*self.color[0]), math.floor(255*self.color[1]), math.floor(255*self.color[2]), 255), outline = None, width = 0)
                draw.ellipse([topLeft, bottomRight], fill = (self.color[0], self.color[1], self.color[2]), outline = None, width = 0)
            
            path = self.getImagePath()

            pathToCheck = path.rsplit('/', 1)[0]
            if not os.path.exists(pathToCheck):
                os.makedirs(pathToCheck)

            im.save(path)

    def calculateArea(self):
        im = Image.open(self.getImagePath())
        w, h = im.size
        maxArea = w * h
        area = 0

        for x in range(w):
            for y in range(h):
                c = im.getpixel((x,y))
                if c == self.color:
                    area += 1

        self.totalArea = area / maxArea

    def getImagePath(self):
        return self.exportPath + str(self.id) + '/img' + '.jpeg'
    
    def getTextPath(self):
        return self.exportPath + str(self.id) + '/info' + '.txt'

    def getCopy(self):
        copiedIndividual = Individual()
        copiedIndividual.fromCopy(deepcopy(self.color), self.circles.copy())
        return copiedIndividual
