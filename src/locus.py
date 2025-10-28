import random 
from typing import Self


class Locus:
    def __init__(self, alleles: tuple):
        self.alleles = alleles

    def __str__(self):
        return f"{self.alleles[0]}{self.alleles[1]}"
    
    @property
    def alelle(self):
        rand = random.randint(0,1)
        return self.alleles[rand]
