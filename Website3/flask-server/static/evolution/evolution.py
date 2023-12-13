from .population import *
from .common import *

populationSize = 10
eliteSize = 1
mutationRate = .5
crossoverRate = .5
tournamentSize = 3

evolving = False

def startEvolution(): #add emoji paths
    print('starting evolution')
    evolving = True

    facePath = getFacePath()
    stickerDirPath = getStickersDirPath()

    print(facePath)

    population = Population(populationSize, eliteSize, mutationRate, crossoverRate, tournamentSize, facePath, stickerDirPath) #add emoji path
    while evolving or population.nGenerations < 50:
        population.evolve()
        print('Gen: ' + str(population.nGenerations) + ' Fitness: ' + str(population.individuals[0].getFitness()))

def stopEvolution():
    global evolving
    evolving = False
    print("stopped evolving")

'''

to-do:

    better area covered calculator
    circle coordinates based on face rectangle
    fitness based on important areas covered (eyes, mouth)

    evaluate based on several images
    web tool using https://pyscript.net? > p5 for graphic stuff

    connect circles - "make masks" - meta balls?
    different objects? - not just circles

    to 3D... script in blender? rhyno?

'''