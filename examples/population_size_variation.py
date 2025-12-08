from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# n simulações com passo de aumento da população de uma pra outra 100 individuos
# taxa de mutação : m
# taxa de duplicação: d
# genepool: pool
# proporção incial de genes
# tamanho inicial do genotype
# tamanho da população

# n/2 simulações exatamente iguais com pouco e n/2 simulações com muitos indivíduos

# Inicialização da simulação
# number_of_generations = int(input("number of generations: "))
# mutation_chance = float(input("Chance de mutação (0-1): "))
# population_size = int(input("Tamanho da população: "))


# Step 2: definir os parâmetros base
# Step 3: preparar uma simulação para cada um dos parâmetros: p0, mut_chance, dup_chance, geneome_size_cost

random.seed(42)
start = time.process_time()

population_sizes_list = np.arange(10, 1010, 100)
simulations_parameters_list = []
duplication_chance = 0.001
for population in population_sizes_list:
    simulations_parameters_list.append((500, 0.0005, population))

avg_final_genotype_size_parameter = []
for scenario in range(len(simulations_parameters_list)):
    simulation_parameters = simulations_parameters_list[scenario]
    number_of_generations, mutation_chance, population_size = simulation_parameters
    print(f"CENARIO: {scenario + 1}/{len(simulations_parameters_list)}")
    number_of_generations, mutation_chance, population_size = simulation_parameters
    number_of_runs = 15
    genepool = [(Locus(("A1")), 1.0, 1),
                (Locus(("A2")), 0.99, 20),
                (Locus(("A3")), 0.95, 10),
                ]

    genotype_A = Genotype(size=1)
    genotype_A[0] = genepool[0][0]
    individual_A1 = Individual(sex='A', genotype=genotype_A)
    population = [
                    [individual_A1, population_size],
                ]

    print(f"INPUT: \n Tamanho da população: {population_size}, \n"
          f"Chance de mutação: {mutation_chance}, \n"
          f"Número de gerações: {number_of_generations}, \n"
          f"Penalidade por gene a mais no genótipo: 0.05, \n"
          f"Chance de duplicação de genes: {duplication_chance}, \n"
          f"Número de corridas por cenário: {number_of_runs}, \n"
          f"População inicial:\n {individual_A1}, quantidade: {population_size}\n"
          f"Genes disponíveis (Identificador 'Locus', fitness, frequência absoluta para amostragem): \n "
          f"(Locus(('A1')), 1.0, 1), (Locus(('A2')), 0.99, 20), (Locus(('A3')), 0.95, 10)"
         )

    genotype_avg_size_per_run = []
    for run in range(number_of_runs):
        print(f"    RUN: {run + 1}")

        first_gen = Generation(population=population,
                               genepool=genepool,
                               duplication_chance=duplication_chance,
                               mutation_chance=mutation_chance)  # 0.00000005

        generation_history = [first_gen]
        genotype_size_history = []

        # Simulação

        for i in range(number_of_generations):

            # Gera próxima geração 
            generation_history.append(generation_history[i].next())
            # print(f"Geração {i}: {generation_history[i]}")

            # Conta o tamanho médio do genótipo das n-1 gerações seguintes
            avg_genotype_size = 0
            for individual in generation_history[i+1]:
                avg_genotype_size += len(individual[0].genotype) * individual[1] / population_size
            genotype_size_history.append(avg_genotype_size)

        print(f"        Tamanho do genótipo ao longo do tempo nesta run: \n {genotype_size_history}")

        genotype_avg_size_per_run.append(genotype_size_history)

    print(f"    FIM DA RUN: {run + 1}")

    avg_genotype_size_history = []
    for i in range(len(genotype_avg_size_per_run[0])):
        avg_genotype_size = 0
        for run in range(number_of_runs):
            avg_genotype_size += genotype_avg_size_per_run[run][i]/len(genotype_avg_size_per_run)
        avg_genotype_size_history.append(avg_genotype_size)
    print(f"    Análise do cenário: {scenario + 1}")
    print(f"        Tamanho do genótipo médio ao longo do tempo: \n{avg_genotype_size_history}")
    avg_final_genotype_size_parameter.append(avg_genotype_size_history[-1])

end = time.process_time()
duration = end - start

print("="*10)
print(f"Galapagos foi explorada uma vez mais!\n Duração da exploração: {duration}")
plt.scatter(population_sizes_list, avg_final_genotype_size_parameter, color="blue")
plt.legend()
plt.title(f"Mutation chance = {mutation_chance},\
          Number of generations = {number_of_generations},\n\
          Duplication chance = 0.001")
plt.xlabel("Tamanho da população")
plt.ylabel("Tamanho genotípico médio final")
plt.savefig("population_variation.png")
plt.show()
