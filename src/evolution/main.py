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