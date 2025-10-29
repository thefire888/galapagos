from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils


# Ensaio VI - Simulando deriva genética

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
gene_pool_b = [Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

population_size = int(input("Tamanho da população: "))
individuals_list = []

for i in range(population_size):
    genotype = Genotype(size=1)
    if i < population_size/2:
        genotype[0] = gene_pool_b[0]
    else:
        genotype[0] = gene_pool_b[2]
    individuals_list.append(Individual(sex=Utils.random_sex(),
                                       genotype=genotype))

first_gen = Generation(size=population_size, individuals=individuals_list)
print(f"Geração 1:\n{first_gen}")
current_gen = first_gen
generations_amount = int(input("Número de gerações a simular: "))

for i in range(generations_amount):
    next_generation = current_gen.next()
    current_gen = next_generation
    print(f"Geração {i + 2}:\n{current_gen}")
