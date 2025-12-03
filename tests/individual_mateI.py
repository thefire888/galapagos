from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual


# Ensaio I - Testando API do Individual e fazendo amor

print("ENSAIO I - Dois pais iguais")

gene_pool = [Locus(('A', 'A')), Locus(('A', 'a')), Locus(('a', 'a'))]

genotype_a = Genotype(size=1)
genotype_a[0] = gene_pool[0]

genotype_b = Genotype(size=1)
genotype_b[0] = gene_pool[0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

individual_c = individual_a.mate(individual_b, 0)
print(f"pai: {individual_a}\n mãe: {individual_b}")
print(f"filho: {individual_c}")
print("filho é igual aos pais?",  individual_c == individual_a or individual_c == individual_b)
print("Esperado: True")
print("FIM DO ENSAIO I")


# Ensaio II - Testando API do Individual e fazendo amor
print()
print("ENSAIO II - pais diferentes, duplicação com 0.01 de chance")
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

individual_c = individual_a.mate(individual_b, 0.1)
print(f"pai: {individual_a}, mãe: {individual_b}")
print(f"filho: {individual_c}")
print(individual_c)
print("FIM DO ENSAIO II")
# Resultado esperado:
# Sexo: M Genótipo: AA BB  Fitness: 1.0


# Ensaio III - Testando API do Individual e fazendo amor
print()
print("ENSAIO III - duplicação com 0.5 de chance")

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

individual_c = individual_a.mate(individual_b, 0.5)
print(f"pai: {individual_a}, mãe: {individual_b}")
print(f"filho: {individual_c}")
print(individual_c)
print("FIM DO ENSAIO III")
# Resultado esperado:
# Sexo: M Genótipo: AA bB Fitness: 1.0
