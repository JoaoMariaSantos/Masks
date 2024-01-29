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

        self.sortByFitness()


    def evolve(self):
        newIndividuals = []

        #elitism
        for i in range(self.eliteSize):
            print("is elite: " + str(i))
            newIndividuals.append(self.individuals[i])

        print("After elitism newIndividuals length is: " + str(len(newIndividuals)))

        #tournament or copy
        for i in range(self.eliteSize, self.populationSize):
            if random.uniform(0,1) <= self.crossoverRate:
                parent1 = self.tournamentSelection().getCopy()
                parent2 = self.tournamentSelection().getCopy()
                child = parent1.crossover(parent2)
                newIndividuals.append(child)
            else:
                newIndividuals.append(self.tournamentSelection().getCopy())

        #mutate
        for i in range(self.eliteSize, self.populationSize):
            newIndividuals[i].mutate(self.mutationRate)

        self.individuals.clear()

        #apply new individuals
        for i in range(self.populationSize):
            self.individuals.append(newIndividuals[i])
            self.individuals[i].id = i

        #evaluate
        for i in range(self.populationSize):
            self.evaluate(self.individuals[i])

        self.sortByFitness()

        #for i in range(len(self.individuals)):
            #print(self.individuals[i].getFitness())

        for i in range(self.populationSize):
            self.individuals[i].id = i
            self.individuals[i].exportImage()
            self.individuals[i].exportInfo()

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

    def getBestFitness(self):
        highestFitness = 0
        highestFitnessIndex = 0

        for i in range(len(self.individuals)):
            if self.individuals[i].getFitness() > highestFitness:
                highestFitness = self.individuals[i].getFitness()
                highestFitnessIndex = i

        return {highestFitness, highestFitnessIndex}
