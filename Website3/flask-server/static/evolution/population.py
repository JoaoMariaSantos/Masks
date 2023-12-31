from .individual import *
from .evaluator import *

class Population:
    populationSize = 0
    eliteSize = 0
    mutationRate = 0
    crossoverRate = 0
    tournamentSize = 0

    facePath = ''

    nGenerations = 0

    individuals = []

    def __init__(self, populationSize, eliteSize, mutationRate, crossoverRate, tournamentSize, facePath, stickerDirPath):
        self.populationSize = populationSize
        self.eliteSize = eliteSize
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate
        self.tournamentSize = tournamentSize
        self.facePath = facePath

        for i in range(self.populationSize):
            self.individuals.append(Individual(facePath, stickerDirPath))
            self.individuals[i].id = i
            self.evaluate(self.individuals[i])


    def evolve(self):
        newIndividuals = []

        #elitism
        for i in range(self.eliteSize):
            newIndividuals.append(self.individuals[i])
            newIndividuals[i].id = i

        #tournament or copy
        for i in range(self.eliteSize, self.populationSize):
            if random.uniform(0,1) <= self.crossoverRate:
                parent1 = self.tournamentSelection()
                parent2 = self.tournamentSelection()
                child = parent1.crossover(parent2)
                newIndividuals.append(child)
            else:
                newIndividuals.append(self.individuals[i].getCopy())

        #mutate
        for i in range(self.eliteSize, self.populationSize):
            newIndividuals[i].mutate(self.mutationRate)
            newIndividuals[i].id = i

        #evaluate
        for i in newIndividuals:
            self.evaluate(i)
        
        #apply new individuals
        for i in range(self.populationSize):
            self.individuals[i] = newIndividuals[i]

        self.sortByFitness()

        for i in range(self.populationSize):
            self.individuals[i].id = i
            self.individuals[i].exportInfo

        self.nGenerations += 1

    def tournamentSelection(self):
        participants = []

        #individuals in tournament
        for i in range(self.tournamentSize):
            participants.append(self.individuals[random.randrange(len(self.individuals))])

        fittest = participants[0]

        #get fittest
        for p in participants:
            if p.fitness > fittest.fitness:
                fittest = p

        return fittest

    def sortByFitness(self):
        self.individuals.sort(key = lambda x: x.getFitness(), reverse = True)

    def evaluate(self, individual):
        individual.exportImage()
        individual.calculateArea()
        evaluate(individual, self.facePath)
