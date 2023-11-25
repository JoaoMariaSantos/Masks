from population import *

populationSize = 10
eliteSize = 1
mutationRate = .5
crossoverRate = .5
tournamentSize = 3

print('Starting')

population = Population(populationSize, eliteSize, mutationRate, crossoverRate, tournamentSize)

while population.nGenerations < 100:
    population.evolve()
    print('Gen: ' + str(population.nGenerations) + ' Fitness: ' + str(population.individuals[0].fitness))

'''
concept:

    generate 3d masks
    generate sheet of stickers from input PNGs
        generate sheet of selected needed emoji stickers
    make someone be identified as someone else - celebrity

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