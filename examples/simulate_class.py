from galapagos.simulation import Simulation
from galapagos.locus import Locus


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
simulation = Simulation(max_generations=300,
                        population_size=1000,
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
simulation = Simulation(max_generations=30,
                        population_size=20,
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
simulation = Simulation(max_generations=30,
                        population_size=20,
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
print("simulação 4 --- frequência inicial incorreta!")
genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 0.99),
            (Locus(("a", "a")), 0.98)
            ]
simulation = Simulation(max_generations=300,
                        population_size=1000,
                        genepool=genepool
                        )

simulation.simulate()
simulation.show()
