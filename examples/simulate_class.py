from galapagos.simulation import Simulation
from galapagos.locus import Locus
from galapagos.genotype import Genotype
from galapagos.individual import Individual
from galapagos.generation import Generation
from galapagos.utils import Utils


print("""
      Simulação 1. Mutação 5%, vantagem pequena, deriva fraca:
      W_{AA}=1, W_{Aa}0,99, W_{aa}=0,98
      N=1000 indivíduos diploides
      Frequência inicial da mutação "A": 5%
      """)

genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 0.99),
            (Locus(("a", "a")), 0.98)
            ]
genotype_A = Genotype(size=1)
genotype_A[0] = genepool[0][0]
individual_A = Individual(sex='M', genotype=genotype_A)

genotype_a = Genotype(size=1)
genotype_a[0] = genepool[2][0]
individual_a = Individual(sex='F', genotype=genotype_a)

population = [
                [individual_A, 50],
                [individual_a, 950]
             ]

first_gen = Generation(population=population)
simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=genepool
                        )
simulation.simulate()
simulation.show()

print("""
      Simulação 2. Mutação em 5%, vantagem pequena, deriva forte:
      W_{AA}=1, W_{Aa}0,99, W_{aa}=0,98
      N=20 indivíduos diploides
      """)
genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 0.99),
            (Locus(("a", "a")), 0.98)
            ]
genotype_A = Genotype(size=1)
genotype_A[0] = genepool[0][0]
individual_A = Individual(sex='M', genotype=genotype_A)

genotype_a = Genotype(size=1)
genotype_a[0] = genepool[2][0]
individual_a = Individual(sex='F', genotype=genotype_a)

population = [
                [individual_A, 1],
                [individual_a, 19]
             ]

first_gen = Generation(population=population)
simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=genepool
                        )
simulation.simulate()
simulation.show()

print("""
      Simulação 3. Mutação em 5%, vantagem grande, deriva forte:
      W_{AA}=1, W_{Aa}1, W_{aa}=0,5
      N=20 indivíduos diploides
      Frequência inicial da mutação "A": 5%
      """
     )
genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 1.0),
            (Locus(("a", "a")), 0.5)
            ]
genotype_A = Genotype(size=1)
genotype_A[0] = genepool[0][0]
individual_A = Individual(sex='M', genotype=genotype_A)

genotype_a = Genotype(size=1)
genotype_a[0] = genepool[2][0]
individual_a = Individual(sex='F', genotype=genotype_a)

population = [
                [individual_A, 1],
                [individual_a, 19]
             ]

first_gen = Generation(population=population)
simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=genepool
                        )
simulation.simulate()
simulation.show()

#
#4. Mutação recém surgida, vantagem fraca, deriva fraca:
#
#W_{AA}=1, W_{Aa}0,99, W_{aa}=0,98
#N=1000 indivíduos diploides
#Frequência inicial da mutação "A": 1/2N = 1/2000
print("""
      simulação 4 --- frequência inicial incorreta!
      4. Mutação recém surgida, vantagem fraca, deriva fraca:
      W_{AA}=1, W_{Aa}0,99, W_{aa}=0,98
      N=1000 indivíduos diploides
      Frequência inicial da mutação "A": 1/2N = 1/2000
      """
     )
genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 0.99),
            (Locus(("a", "a")), 0.98)
            ]
genotype_Aa = Genotype(size=1)
genotype_Aa[0] = genepool[1][0]
individual_Aa = Individual(sex='M', genotype=genotype_A)

genotype_a = Genotype(size=1)
genotype_a[0] = genepool[2][0]
individual_a = Individual(sex='F', genotype=genotype_a)

population = [
                [individual_A, 1],
                [individual_a, 999]
             ]

first_gen = Generation(population=population)
simulation = Simulation(max_generations=150,
                        first_generation=first_gen,
                        genepool=genepool
                        )
simulation.simulate()
simulation.show()
