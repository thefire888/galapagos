from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils

genepool = [
                (Locus(('A', 'A')), 0.50),
                (Locus(('A', 'a')), 0.50),
                (Locus(('a', 'a')), 1.0)
              ]

genotype_a = Genotype(size=1)
genotype_a[0] = genepool[0][0]

genotype_b = Genotype(size=1)
genotype_b[0] = genepool[2][0]

individual_a = Individual(sex='M', genotype=genotype_a)
individual_b = Individual(sex='F', genotype=genotype_a)
individual_c = Individual(sex='F', genotype=genotype_b)
individual_d = Individual(sex='M', genotype=genotype_b)

population = [
              [individual_a, 1000],
              [individual_b, 1000],
              [individual_c, 1000],
              [individual_d, 1000]
             ]

first_gen = Generation(population=population, genepool=genepool)

simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=genepool
                        )

simulation.simulate()
simulation.show()


