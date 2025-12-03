from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils


# n simulações com passo de aumento da população de uma pra outra 100 individuos
# taxa de mutação : m
# taxa de duplicação: d
# genepool: pool
# proporção incial de genes
# tamanho inicial do genotype
# tamanho da população

# n/2 simulações exatamente iguais com pouco e n/2 simulações com muitos indivíduos

n = int(input("number of simulations: "))


genepool = [(Locus(("A1")), 1.0),
            (Locus(("A2")), 1.0),
            (Locus(("A3")), 1.0)
            ]

genotype_A = Genotype(size=1)
genotype_A[0] = genepool[0][0]
individual_A1F = Individual(sex='F', genotype=genotype_A)
individual_A1M = Individual(sex='M', genotype=genotype_A)

population = [
                [individual_A1F, 50],
                [individual_A1M, 50]
             ]

first_gen = Generation(population=population,
                       genepool=genepool,
                       duplication_chance=0.01,
                       mutation_chance=0.00000005)

generation_history = [first_gen]

for i in range(n):
    generation_history.append(generation_history[i].next())
    print(f"Geração {i}: {generation_history[i]}")

