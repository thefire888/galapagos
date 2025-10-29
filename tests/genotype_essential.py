import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from locus import Locus
from genotype import Genotype

# Teste Unitário da classe Genotype
# Resultado esperado: printa o genótipo criado
locus_a = Locus(('A', 'a'))
locus_b = Locus(('B', 'b'))

genotype = Genotype(size=2)
genotype[0] = locus_a
genotype[1] = locus_b
print(genotype)
