from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils
import matplotlib.pyplot as plt

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


simulations_parameters_list =[
                                (800, 0.005, 100),
                                (800, 0.005, 1000)
                             ]
for simulation_parameters in simulations_parameters_list:
    number_of_generations, mutation_chance, population_size = simulation_parameters
    number_of_runs = 15
    genepool = [(Locus(("A1")), 1.0, 1),
                (Locus(("A2")), 0.99, 20),
                (Locus(("A3")), 0.95, 10),
                ]

    genotype_A = Genotype(size=1)
    genotype_A[0] = genepool[0][0]
    individual_A1F = Individual(sex='F', genotype=genotype_A)
    individual_A1M = Individual(sex='M', genotype=genotype_A)

    genotype_avg_size_per_run = []
    for run in range(number_of_runs):
        population = [
                        [individual_A1F, population_size],
                     ]

        first_gen = Generation(population=population,
                               genepool=genepool,
                               duplication_chance=0.001,
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

        genotype_avg_size_per_run.append(genotype_size_history)

        plt.scatter(list(range(number_of_generations)), genotype_size_history, s=2, alpha=0.6)

    avg_genotype_size_history = []
    for i in range(len(genotype_avg_size_per_run[0])):
        avg_genotype_size = 0
        for run in range(number_of_runs):
            avg_genotype_size += genotype_avg_size_per_run[run][i]/len(genotype_avg_size_per_run)
        avg_genotype_size_history.append(avg_genotype_size)

    plt.plot(list(range(number_of_generations)), avg_genotype_size_history, label="Corrida média")
    plt.axhline(y=avg_genotype_size_history[-1], label="Tamanho genotípico final da corrida média")
    plt.legend()
    plt.title(f"Population size = {population_size},\
              Number of generations = {number_of_generations},\n\
              Mutation chance = {mutation_chance},\
              Duplication chance = 0.001")
    plt.xlabel("Geração")
    plt.ylabel("Tamanho genotípico médio")
    plt.show()
