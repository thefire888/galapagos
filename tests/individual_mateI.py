import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from locus import Locus
from genotype import Genotype
from individual import Individual


# Ensaio I - Testando API do Individual e fazendo amor

gene_pool = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]

genotype_a = Genotype(size=1)
genotype_a[0] = gene_pool[0]

genotype_b = Genotype(size=1)
genotype_b[0] = gene_pool[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

individual_c = individual_a.mate(individual_b)
print(individual_c)


# Ensaio II - Testando API do Individual e fazendo amor

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
gene_pool_b = [Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

genotype_a = Genotype(size=2)
genotype_a[0] = gene_pool_a[0]
genotype_a[1] = gene_pool_b[0]

genotype_b = Genotype(size=2)
genotype_b[0] = gene_pool_a[0]
genotype_b[1] = gene_pool_b[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

individual_c = individual_a.mate(individual_b)
print(individual_c)
# Resultado esperado:
# Sexo: M Genótipo: AA BB  Fitness: 1.0


# Ensaio III - Testando API do Individual e fazendo amor

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
gene_pool_b = [Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

genotype_a = Genotype(size=2)
genotype_a[0] = gene_pool_a[0]
genotype_a[1] = gene_pool_b[2]

genotype_b = Genotype(size=2)
genotype_b[0] = gene_pool_a[0]
genotype_b[1] = gene_pool_b[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

individual_c = individual_a.mate(individual_b)
print(individual_c)
# Resultado esperado:
# Sexo: M Genótipo: AA bB Fitness: 1.0
