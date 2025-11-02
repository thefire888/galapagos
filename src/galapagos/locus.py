import random
from typing import Self


class Locus:
    def __init__(self, alleles: tuple):
        self.alleles = alleles  

    def __str__(self):
        canon_alleles = sorted(self.alleles)
        return f"{canon_alleles[0]}{canon_alleles[1]}"

    def __eq__(self, other: Self) -> bool:
        return set(self.alleles) == set(other.alleles)

    @property
    def alelle(self):
        rand = random.randint(0, 1)
        return self.alleles[rand]
