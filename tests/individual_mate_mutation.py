from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual


print("ENSAIO I - mutação com 0.5 de chance")

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a')),
               Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

genotype_a = Genotype(size=1)
genotype_a[0] = gene_pool_a[0]

genotype_b = Genotype(size=1)
genotype_b[0] = gene_pool_a[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

individual_c = individual_a.mate(individual_b,
                                 mutation_chance=0.5,
                                 duplication_chance=0.0,
                                 genepool=gene_pool_a)
print(f"Pai: {individual_a}\nMãe: {individual_b}")
print(f"filho: {individual_c}")
print("FIM DO ENSAIO III")
