from population import *

populationSize = 30
eliteSize = 2
mutationRate = .5
crossoverRate = .5
tournamentSize = 5

population = Population(populationSize, eliteSize, mutationRate, crossoverRate, tournamentSize)

while population.nGenerations < 100:
    population.evolve()
    print('Gen: ' + str(population.nGenerations) + ' Fitness: ' + str(population.individuals[0].fitness))