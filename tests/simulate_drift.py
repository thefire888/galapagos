from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils

gene_pool_a = [
                (Locus(('A', 'A')), 1.0),
                (Locus(('A', 'a')), 1.0),
                (Locus(('a', 'a')), 1.0)
              ]

genotype_a = Genotype(size=1)
genotype_a[0] = gene_pool_a[0][0]

genotype_b = Genotype(size=1)
genotype_b[0] = gene_pool_a[2][0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_b)

population = [
              [individual_a, 30],
              [individual_b, 30]
             ]

first_gen = Generation(population=population)

simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=gene_pool_a
                        )

simulation.simulate()
simulation.show()
