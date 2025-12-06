"""
Defines the current individuals in the population.
Responsible for generating the next generation
"""
from galapagos.utils import Utils
from typing import Self
from collections import defaultdict


class Generation:
    def __init__(self,
                 population: list = [],
                 genepool: list = [],
                 duplication_chance: float = 0.0,
                 mutation_chance: float = 0.0,
                 equal_mutation_odds: bool = False
                ):
        """
            uma geração define os indivíduos da população em um dado período de tempo.
            args:
                population (list) = uma lista de tuplas com (tipo de indivíduo, quantidade igual na população)
                genepool (list) = uma lista dos tuplas com (Carctére representativo do alelo, fitness)
        """
        self.__genepool = genepool
        self.population = population 
        self.duplication_chance = duplication_chance
        self.mutation_chance = mutation_chance
        self.equal_mutation_odds = equal_mutation_odds

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
        next_gen = Generation(genepool=self.genepool,
                              duplication_chance=self.duplication_chance,
                              mutation_chance=self.mutation_chance,
                              equal_mutation_odds=self.equal_mutation_odds
                             )

        next_gen_individual_counts = defaultdict(int)
        for i in range(len(self)):
            some_individual = Utils.select_individual(self.population)
            newborn = some_individual.clone(next_gen.duplication_chance,
                                            next_gen.mutation_chance,
                                            next_gen.genepool,
                                            equal_mutation_odds=self.equal_mutation_odds
                                           )
            newborn.update_fitness(self.genepool)

            next_gen_individual_counts[newborn] += 1

        next_gen.population = [
            [individual, individual_count] for individual, individual_count in next_gen_individual_counts.items()
        ]

        return next_gen

