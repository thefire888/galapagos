import random
from typing import Self


class Locus:
    def __init__(self, alleles: tuple):
        self.alleles = alleles  

    def __str__(self):
        canon_alleles = sorted(self.alleles)
        return_str = f""
        for i in canon_alleles:
            return_str += f"{i}"
        return return_str

    def __eq__(self, other: Self) -> bool:
        return set(self.alleles) == set(other.alleles)

    @property
    def alelle(self):
        rand = random.randint(0, 1)
        return self.alleles[rand]
