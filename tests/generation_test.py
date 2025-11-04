from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils

# Ensaio IV - Testando API da Geração

gene_pool_a = [
                (Locus(('A', 'A')), 1.0), 
                (Locus(('A', 'a')), 1.0), 
                (Locus(('a', 'a')), 1.0)
              ]

gene_pool_b = [
                (Locus(('B', 'B')), 1.0), 
                (Locus(('B', 'b')), 1.0), 
                (Locus(('b', 'b')), 1.0)
              ]

genotype_a = Genotype(size=2)
genotype_a[0] = gene_pool_a[0][0]
genotype_a[1] = gene_pool_b[0][0]

genotype_b = Genotype(size=2)
genotype_b[0] = gene_pool_a[0][0]
genotype_b[1] = gene_pool_b[0][0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

population = [ 
              [individual_a, 2], 
              [individual_b, 2]
             ]

first_gen = Generation(population=population)

print(first_gen)
print(first_gen.next())
# Resultado esperado:
# Indivíduo 0: Sexo: M Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 1: Sexo: F Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 2: Sexo: F Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
# Indivíduo 3: Sexo: M Genótipo: ('A', 'A')('B', 'B') Fitness: 1.0
