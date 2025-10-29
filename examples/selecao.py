import sys
import os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from locus import Locus
from genotype import Genotype
from individual import Individual
from generation import Generation
from utils import Utils


gene_pool = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
population_size = 10
first_individuals_list = []

for i in range(0, population_size):
    new_sex = Utils.random_sex()
    new_genotype = Genotype(size=1)
    new_genotype[0] = gene_pool[random.randint(0, 2)]
    new_fitness = 1.0
    if new_genotype[0] == gene_pool[2]:
        new_fitness = 0.5
    new_individual = Individual(sex=new_sex,
                                genotype=new_genotype,
                                fitness=new_fitness)
    first_individuals_list.append(new_individual)
first_generation = Generation(size=population_size,
                              individuals=first_individuals_list)

print(f"Primeira geração:\n{first_generation}")

generations_amount = 5
current_generation = first_generation
for i in range(0, generations_amount):
    new_generation = current_generation.next()
    print(f"Geração{i + 2}:\n {new_generation}")
    current_generation = new_generation

# TODO: como transmitir o fitness para frente?
