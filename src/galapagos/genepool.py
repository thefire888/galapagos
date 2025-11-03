from galapagos.generation import Generation
from galapagos.utils import Utils
from galapagos.genotype import Genotype
from galapagos.individual import Individual

class Genepool:
    def __init__(self, 
                 genotypes: list, 
                 fitnesses: list
                 ):
        self.genotypes = genotypes
        self.fitnesses = fitnesses

