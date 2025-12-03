"""
Defines an individual to simulate.
"""
import random
from galapagos.genotype import Genotype
from galapagos.locus import Locus
from galapagos.utils import Utils
from typing import Self


class Individual:
    def __init__(self, sex: str, genotype: Genotype,
                 fitness: float = 1.0):
        self.__fitness = fitness
        self.__sex = sex
        self.genotype = genotype

    def __str__(self):
        return (f"Sexo: {self.sex} Genótipo: {self.genotype}"
                f"Fitness: {self.__fitness}")

    def __eq__(self, other):
        return (self.fitness == other.fitness) and (self.sex == other.sex) and (self.genotype == other.genotype)

    def __hash__(self):
        return hash((self.fitness, self.sex, self.genotype))

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

    @property
    def sex(self):
        return self.__sex

    def clone(self,
              duplication_chance: float = 0.0,
              mutation_chance: float = 0.0,
              genepool: list = []) -> Self:

        new_genotype = Genotype(size=len(self.genotype))

        for i in range(len(self.genotype)):
            locus = self.genotype[i]
            new_genotype[i] = locus

        # gene duplication and mutation
        for i in range(len(new_genotype)):
            duplication_dice = random.uniform(0, 1)
            if duplication_dice < duplication_chance:
                new_genotype.size += 1
                new_genotype.append(new_genotype[i])
            mutation_dice = random.uniform(0, 1)
            if mutation_dice < mutation_chance:
                gene_to_mutate_dice = random.randint(0, len(genepool) - 1)
                gene_to_mutate = genepool[gene_to_mutate_dice][0]
                new_genotype[i] = gene_to_mutate

        new_sex = Utils.random_sex()
        newborn = Individual(new_sex, new_genotype)

        return newborn

    def update_fitness(self, genepool):
        if genepool:
            self.fitness = 0.0
            for locus in self.genotype:
                idx = [gene[0] for gene in genepool].index(locus)
                self.fitness += genepool[idx][1]/len(self.genotype)
