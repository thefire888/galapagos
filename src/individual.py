"""
Defines an individual to simulate.
"""
from genotype import Genotype
from locus import Locus
from typing import Self
from utils import Utils


class Individual:
    def __init__(self, sex: str, genotype: Genotype,
                 fitness: float = 1.0):
        self.__fitness = fitness
        self.__sex = sex
        self.genotype = genotype

    def __str__(self):
        return (f"Sexo: {self.sex} Genótipo: {self.genotype}"
                f"Fitness: {self.__fitness}")

    @property
    def fitness(self):
        return self.__fitness

    @property
    def sex(self):
        return self.__sex

    def mate(self, other: Self) -> Self:
        new_genotype = Genotype(size=len(self.genotype))
        for i in range(len(self.genotype)):
            locus = Locus(
                (self.genotype[i].alelle,
                 other.genotype[i].alelle)
            )
            new_genotype[i] = locus

        new_sex = Utils.random_sex()
        newborn = Individual(new_sex, new_genotype)

        return newborn
