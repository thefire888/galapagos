from galapagos.generation import Generation
from galapagos.utils import Utils
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from plotnine import *
import matplotlib.pyplot as plt
import numpy as np
import polars as pl

class Simulation:
    def __init__(self, 
                 max_generations: int, 
                 population_size: int,
                 genepool: list
                 ):
        self.max_generations = max_generations
        self.population_size = population_size
        self.genepool = genepool

        first_individuals_list = []

        for i in range(population_size):
            new_sex = Utils.random_sex()
            new_genotype = Genotype(size=1)
            new_genotype[0] = self.genepool[0][0] if i < population_size/2 else self.genepool[2][0]
            new_fitness = self.genepool[0][1] if i < population_size/2 else self.genepool[2][1]
            new_individual = Individual(sex=new_sex,
                                        genotype=new_genotype,
                                        fitness=new_fitness)
            first_individuals_list.append(new_individual)

        self.first_generation = Generation(size=population_size,
                                      individuals=first_individuals_list,
                                      genepool=self.genepool
                                      )
        self.generation_history = [self.first_generation]

    def simulate(self):
        for i in range(self.max_generations):
            new_generation = self.generation_history[i].next()
            self.generation_history.append(new_generation)

    def show(self):
        data = []
        for index, gen in enumerate(self.generation_history):
            for i in self.genepool:
                locus = i[0]
                freq = gen.get_locus_frequency(locus)
                data.append({"generation": index,
                             "genotype": str(locus), #TODO: Ajustar str do Locus para ordem canônica
                             "frequency": freq
                    })

        df = pl.DataFrame(data)
        print(df)
        (
            ggplot(df, aes(x="generation", y="frequency", color="genotype"))
            + geom_bar(position="fill")
        ).show()
