from galapagos.simulation import Simulation
from galapagos.locus import Locus

genepool = [(Locus(("A", "A")), 1.0),
            (Locus(("A", "a")), 1.5),
            (Locus(("a", "a")), 1.0)
            ]
simulation = Simulation(max_generations=300,
                        population_size=200,
                        genepool=genepool
                        )

simulation.simulate()
simulation.show()
