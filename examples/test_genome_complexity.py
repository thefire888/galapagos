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
                                (5000, 0.0005, 100),
                                (50, 0.0005, 10000)
                             ]
for simulation_parameters in simulations_parameters_list:
    number_of_generations, mutation_chance, population_size = simulation_parameters
    genepool = [(Locus(("A1")), 1.0),
                (Locus(("A2")), 0.99),
                (Locus(("A3")), 0.95)
                ]

    genotype_A = Genotype(size=1)
    genotype_A[0] = genepool[0][0]
    individual_A1F = Individual(sex='F', genotype=genotype_A)
    individual_A1M = Individual(sex='M', genotype=genotype_A)

    population = [
                    [individual_A1F, population_size],
                 ]

    first_gen = Generation(population=population,
                           genepool=genepool,
                           duplication_chance=0.1,
                           mutation_chance=mutation_chance)  # 0.00000005

    generation_history = [first_gen]
    genotype_size_history = []

    # Simulação

    for i in range(number_of_generations):

        # Gera próxima geração 
        generation_history.append(generation_history[i].next())
        # print(f"Geração {i}: {generation_history[i]}")

        # Conta o tamanho médio do genótipo das n-1 gerações seguintes
        medium_genotype_size = 0
        for individual in generation_history[i+1]:
            medium_genotype_size += len(individual[0].genotype) * individual[1]
        genotype_size_history.append(medium_genotype_size / population_size)

    # Visualização de resultados

    plt.scatter(list(range(number_of_generations)), genotype_size_history)
    plt.show()
    # print(f"{generation_history[number_of_generations - 1]}")
