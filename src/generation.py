"""
Defines the current individuals in the population.
Responsible for generating the next generation
"""
from typing import Self
from utils import Utils


class Generation:
    def __init__(self, size: int, individuals: list = []):
        self.__size = size
        self.individuals = individuals if individuals else [None] * size

    def __len__(self):
        return self.__size

    def __getitem__(self, key):
        return self.individuals[key]

    def __setitem__(self, key, value):
        self.individuals[key] = value

    def __str__(self):
        return_string = ""
        for i in range(len(self)):
            return_string += f"Indivíduo {i}: {self[i]}\n"
            return return_string

    def next(self) -> Self:
        next_gen = Generation(size=len(self))
        male_available_individuals = []
        female_available_individuals = []
        for individual in self.individuals:
            if individual.sex == "M":
                male_available_individuals.append(individual)
            else:
                female_available_individuals.append(individual)

        for i in range(len(self.individuals)):
            father = Utils.select_individual(male_available_individuals)
            mother = Utils.select_individual(female_available_individuals)
            newborn = father.mate(mother)
            next_gen[i] = newborn

        return next_gen
