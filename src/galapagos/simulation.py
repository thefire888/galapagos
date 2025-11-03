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

    def _selection_model(self) -> list:
        # TODO: Rever referência, me parece errado
        data_theory = []
        first_gen = self.first_generation
        freq_prev = {}
        freq_theory = {}

        for locus, _ in self.genepool:
            freq_prev[str(locus)] = first_gen.get_locus_frequency(locus)

        for g in range(self.max_generations):
            fitness_avg = 0

            # Calculates fitness_avg
            for locus, fitness in self.genepool:
                fitness_avg += freq_prev[str(locus)] * fitness

            # Calculate expected frequency
            for locus, fitness in self.genepool:
                freq_theory[str(locus)] = freq_prev[str(locus)] * fitness / fitness_avg
                data_theory.append({
                    "generation": g + 1,
                    "genotype": str(locus),
                    "expected_frequency": freq_theory[str(locus)]
                })
            freq_prev = freq_theory
        return data_theory

    def simulate(self):
        gene_lines = [
            f"Gene: {str(gene)}, Fitness: {fitness}"
            for gene, fitness in self.genepool
        ]

        print(f"""INPUT:
              maximum number of generations: {self.max_generations},
              population size: {self.population_size},
              available genes: {gene_lines}
              """
             )
        for i in range(self.max_generations):
            new_generation = self.generation_history[i].next()
            self.generation_history.append(new_generation)
            self._process_generation_data(new_generation, index=i + 1)

    def show(self):

        df_simu = pl.DataFrame(self.data)
        # df_theory = pl.DataFrame(self._selection_model())
        (
            ggplot(df_simu, aes(x="generation", color="genotype"))
            + geom_line(aes(y="frequency"), size=1)
            # + geom_line(data=df_theory,
            #            mapping=aes(y="expected_frequency", linetype="'Teórico'"),
            #            size=1
            #            )
            + labs(x="Geração", y="Frequência", color="Genótipo")

            # + scale_linetype_manual(
            #     name="Fonte dos Dados",
            #     values={"Simulado": "solid", "Teórico": "dashed"}
            # )
        ).show()
