import random

from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils


gene_pool = [(Locus(('A', 'A')), 1.0), 
             (Locus(('A', 'a')), 1.0), 
             (Locus(('a', 'a')), 0.8)
             ]
population_size = int(input("Dê o tamanho da população inicial:\n"))
first_individuals_list = []

for i in range(population_size):
    new_sex = Utils.random_sex()
    new_genotype = Genotype(size=1)
    new_genotype[0] = gene_pool[0][0] if i < population_size/2 else gene_pool[2][0]
    new_fitness = gene_pool[0][1] if i < population_size/2 else gene_pool[2][1]
    new_individual = Individual(sex=new_sex,
                                genotype=new_genotype,
                                fitness=new_fitness)
    first_individuals_list.append(new_individual)
first_generation = Generation(size=population_size,
                              individuals=first_individuals_list,
                              genepool=gene_pool
                              )

print(f"Primeira geração:\n{first_generation}")

generations_amount = int(input("Dê o número máximo de gerações:\n"))
current_generation = first_generation
for i in range(generations_amount):
    new_generation = current_generation.next()
    print(f"Geração{i + 2}:\n {new_generation}")
    current_generation = new_generation

# TODO: como transmitir o fitness para frente?
