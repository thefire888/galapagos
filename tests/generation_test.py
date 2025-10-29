from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils

# Ensaio IV - Testando API da Geração

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
gene_pool_b = [Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

genotype_a = Genotype(size=2)
genotype_a[0] = gene_pool_a[0]
genotype_a[1] = gene_pool_b[0]

genotype_b = Genotype(size=2)
genotype_b[0] = gene_pool_a[0]
genotype_b[1] = gene_pool_b[0]

genotype_c = Genotype(size=2)
genotype_c[0] = gene_pool_a[0]
genotype_c[1] = gene_pool_b[0]

genotype_d = Genotype(size=2)
genotype_d[0] = gene_pool_a[0]
genotype_d[1] = gene_pool_b[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)
individual_c = Individual(sex='F', genotype=genotype_c)
individual_d = Individual(sex='M', genotype=genotype_d)

individuals = [individual_a, individual_b, individual_c, individual_d]

first_gen = Generation(size=4, individuals=individuals)

print(first_gen)
# Resultado esperado:
# Indivíduo 0: Sexo: M Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 1: Sexo: F Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 2: Sexo: F Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 3: Sexo: M Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0


# Ensaio V - Testando API da Geração e organizando orgias

gene_pool_a = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]
gene_pool_b = [Locus(('B', 'B')), Locus(('B', 'b')), Locus(('b', 'b'))]

genotype_a = Genotype(size=2)
genotype_a[0] = gene_pool_a[0]
genotype_a[1] = gene_pool_b[0]

genotype_b = Genotype(size=2)
genotype_b[0] = gene_pool_a[0]
genotype_b[1] = gene_pool_b[0]

genotype_c = Genotype(size=2)
genotype_c[0] = gene_pool_a[0]
genotype_c[1] = gene_pool_b[0]

genotype_d = Genotype(size=2)
genotype_d[0] = gene_pool_a[0]
genotype_d[1] = gene_pool_b[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)
individual_c = Individual(sex='F', genotype=genotype_c)
individual_d = Individual(sex='M', genotype=genotype_d)

individuals = [individual_a, individual_b, individual_c, individual_d]

first_gen = Generation(size=4, individuals=individuals)

print(f"Geração 1:\n{first_gen}")
print(f"Geração 2:\n{first_gen.next()}")
print(f"Geração 3:\n{first_gen.next().next()}")
