from population import *

populationSize = 15
eliteSize = 1
mutationRate = .5
crossoverRate = .5
tournamentSize = 5

population = Population(populationSize, eliteSize, mutationRate, crossoverRate, tournamentSize)

while population.nGenerations < 50:
    population.evolve()
    print(str(population.nGenerations) + '  ' + str(population.individuals[0].fitness) + '  ' + str(population.individuals[0].totalArea))