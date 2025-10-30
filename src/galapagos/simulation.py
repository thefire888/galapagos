from galapagos.generation import Generation
from galapagos.utils import Utils
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from plotnine import *
from plotnine.data import anscombe_quartet
import matplotlib.pyplot as plt
import numpy as np

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
        for i in self.genepool:
            locus = i[0]
            loci = []
            for gen in self.generation_history:
                loci.append(gen.get_locus_frequency(locus))

            generation_count = np.linspace(0,
                                           len(self.generation_history) - 1, 
                                           len(self.generation_history))

            plt.scatter(generation_count, 
                        loci, 
                        alpha=0.2, 
                        s=10
                        )
        plt.figure(figsize=(10, 7))
        plt.xlabel('Frequência Alelo "ref" ($p$)', fontsize=12)
        plt.ylabel('Frequência Genotípica', fontsize=12)
        plt.title('Observado vs. Esperado (Equilíbrio de Hardy-Weinberg) \n Braço Curto', fontsize=14)
        plt.grid(True, linestyle=':', alpha=0.2)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
        plt.tight_layout(rect=[0, 0.05, 1, 1]) # Ajusta espaço para a legenda

        plt.show()

        ggplot(anscombe_quartet, aed(x="x", y="y")) + geom_point()




