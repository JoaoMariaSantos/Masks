import random
import math
import os
from .common import *
from PIL import Image, ImageDraw
from copy import deepcopy

class Individual:
    exportPath = 'static/evolution/individuals/'
    #referencePath = 'C:/Files/UC/5.1/LDC/REPO/Masks/Website3/flask-server/static/evolution/reference/portrait-white-man-isolated_5387.png'
    referencePath = ''
    stickerDirPath = ''
    stickers = []
    fitness = 0
    id = 0
    maxStickers = 5
    info = {
        "fitness" : 0, 
        "distance" : 0,
        "area" : 0
    }

    def __init__(self, referencePath, stickerDirPath):
        self.stickers.append(createSticker())
        self.referencePath = referencePath
        self.stickerDirPath = stickerDirPath
        self.limitStickers()

    def fromCopy(self, stickers, referencePath, stickerDirPath, info):
        self.stickers = stickers
        self.referencePath = referencePath
        self.stickerDirPath = stickerDirPath
        self.info = info
        self.limitStickers()

    def setInfo(self, fitness, distance, area):
        self.info["fitness"] = fitness
        self.info["distance"] = distance
        self.info["area"] = area

    def exportInfo(self):
        lines = ['fitness: ' + str(self.info["fitness"]), 
                 'distance: ' + str(self.info["distance"]),
                 'area: ' + str(self.info["area"])]
        with open(self.getTextPath(), 'w') as f:
            f.write('\n'.join(lines))
        
    def limitStickers(self):
        self.stickers = self.stickers[:self.maxStickers]

    def mutate(self, mutationRate):

        if random.uniform(0,1) < (mutationRate/2):
            if len(self.stickers) > 3 and random.uniform(0,1) < .5:
                self.stickers.pop(random.randrange(len(self.stickers))) 
            elif len(self.stickers) < self.maxStickers:
                self.stickers.append(createSticker())

        for c in self.stickers:
            if random.uniform(0,1) < mutationRate:
                c['x'] = clamp(c['x'] + random.uniform(-0.1, 0.1), 0, 1)
                c['y'] = clamp(c['y'] + random.uniform(-0.1, 0.1), 0, 1)
                c['radius'] = clamp(c['radius'] + random.uniform(-0.1, 0.1), 0, 1)
                c['rotation'] = clamp(c['rotation'] + random.uniform(-0.1, 0.1), 0, 1)
                c['id'] = clamp(c['id'] + random.uniform(-0.1, 0.1), 0, 1)
    
    def crossover(self, individual):
        child = Individual(self.referencePath, self.stickerDirPath)
        child.stickers = []

        for i in range(len(self.stickers)):
            if len(child.stickers) >= self.maxStickers:
                break
            if random.uniform(0,1) < 0.5:
                child.stickers.append(self.stickers[i])
            elif i < len(individual.stickers):
                child.stickers.append(individual.stickers[i])

        child.limitStickers()
        return child

    def exportImage(self):

        background = Image.open(self.referencePath)
        images = []
        for sticker in self.stickers:

            imgToOpen = str(math.floor(sticker['id'] * 4)) + '.png'

            try:
                overlay = Image.open(self.stickerDirPath + '/' + imgToOpen)
                images.append(overlay)
            except FileNotFoundError as e:
                pass

        w, h = background.size

        result = Image.new("RGBA", background.size, (0, 0, 0, 0))
        result.paste(background, (0,0))

        index = 0

        self.limitStickers()

        for sticker in self.stickers:
            x = math.floor(sticker['x'] * w)
            y = math.floor(sticker['y'] * h)
            clampedRadius = clamp(sticker['radius'], 0.05, 0.3)
            radius = math.floor(clampedRadius * w) + 1
            
            images[index] = images[index].resize((radius, radius))
            images[index] = images[index].rotate(sticker['rotation'] * 360)

            result.paste(images[index], (x, y), images[index])    
            
            index += 1
            if index >= len(images):
                 index = len(images) - 1

        path = self.getImagePath()

        pathToCheck = path.rsplit('/', 1)[0]
        if not os.path.exists(pathToCheck):
            os.makedirs(pathToCheck)

            # Check the file extension and save accordingly
        _, file_extension = os.path.splitext(path)
        if file_extension.lower() == '.jpg' or file_extension.lower() == '.jpeg':
            result = result.convert("RGB")  # Convert to RGB before saving as JPEG
            result.save(path)

    #TODO: fix calculatearea
    def calculateArea(self):        
        area = 0
        
        for sticker in self.stickers:
            area = area + (sticker['radius'] * sticker['radius'])

        self.info['area'] = area

    def getImagePath(self):
        return self.exportPath + str(self.id) + '/img' + '.jpeg'
    
    def getTextPath(self):
        return self.exportPath + str(self.id) + '/info' + '.txt'

    def getCopy(self):
        copiedIndividual = Individual(self.referencePath, self.stickerDirPath)
        copiedIndividual.fromCopy(self.stickers.copy(), self.referencePath, self.stickerDirPath, self.info.copy())
        return copiedIndividual
    
    def getFitness(self):
        return float(self.info["fitness"])
