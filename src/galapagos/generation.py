"""
Defines the current individuals in the population.
Responsible for generating the next generation
"""
from galapagos.utils import Utils
from typing import Self


class Generation:
    def __init__(self, population: list = [], genepool: list = []):
        self.__genepool = genepool
        self.population = population 

    def __len__(self):
        partial_size = 0
        for item in self.population:
            individual = item[0]
            individual_count = item[1]
            partial_size += individual_count
        return partial_size

    def __getitem__(self, key):
        return self.population[key]

    def __setitem__(self, key, value):
        self.population[key] = value

    def __str__(self):
        return_string = ""
        for i in range(len(self.population)):
            return_string += f"Indivíduo: {self[i][0]} Quantidade: {self[i][1]} \n"
        return return_string

    @property
    def genepool(self):
        return self.__genepool

    def next(self) -> Self:
        next_gen = Generation(genepool=self.genepool)
        male_available_individuals = []
        female_available_individuals = []
        for item in self.population:
            individual = item[0]
            if individual.sex == "M":
                male_available_individuals.append(item)
            else:
                female_available_individuals.append(item)

        for i in range(len(self)):
            father = Utils.select_individual(male_available_individuals)
            mother = Utils.select_individual(female_available_individuals)
            newborn = father.mate(mother)
            newborn.update_fitness(self.genepool)

            newborn_in_pop = False
            for item in next_gen.population:
                individual = item[0]
                if newborn == individual:
                    item[1] += 1  # It seems like Python doesnt like object reference
                    newborn_in_pop = True
            
            if not newborn_in_pop:
                next_gen.population.append([newborn, 1])

        return next_gen

