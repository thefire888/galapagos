from galapagos.simulation import Simulation
from galapagos.locus import Locus

genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 1.0),
            (Locus(("a", "a")), 1.0)
            ]
simulation = Simulation(max_generations=100,
                        population_size=2000,
                        genepool=genepool
                        )

simulation.simulate()
simulation.show()
