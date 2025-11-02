from galapagos.generation import Generation
from galapagos.utils import Utils
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from plotnine import *
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
        self.data = []

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

    def _process_generation_data(self, generation, index: int):
        for i in self.genepool:
            locus = i[0]
            freq = generation.get_locus_frequency(locus)
            self.data.append({
                "generation": index,
                "genotype": str(locus),
                "frequency": freq
            })

    def simulate(self):
        for i in range(self.max_generations):
            new_generation = self.generation_history[i].next()
            self.generation_history.append(new_generation)
            self._process_generation_data(new_generation, index=i + 1)

    def show(self):
        df = pl.DataFrame(self.data)
        (
            ggplot(df, aes(x="generation", y="frequency", color="genotype"))
            + geom_line(size=1)
        ).show()
