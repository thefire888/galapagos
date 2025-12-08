import pytest
from galapagos_evo import Locus, Genotype, Individual, Generation
import sys

print(f"Python version: {sys.version}")


def test_locus_hashing_and_equality():
    l1 = Locus(["A", "a"])
    l2 = Locus(["a", "A"])
    l3 = Locus(["A", "b"])

    # a) __eq__ e __hash__ (se forem iguais, devem ter o mesmo hash)
    assert l1 == l2, "Loci com a mesma composição devem ser iguais."
    assert hash(l1) == hash(l2), "Loci iguais devem ter o mesmo hash."
    assert l1 != l3, "Loci diferentes devem ser desiguais."
    
    # b) __str__ (Verifica se a representação é canônica)
    assert str(l1) == "Aa", "__str__ deve ser canônico."

def test_individual_update_fitness():
    
    locus_AA = Locus(["A", "A"])
    locus_Aa = Locus(["A", "a"])
    locus_bb = Locus(["b", "b"])

    genotype_good = Genotype(size=1)
    genotype_good.append(locus_Aa)
    
    genotype_bad = Genotype(size=1)
    genotype_bad.append(locus_bb)

    genepool_py = [
        (locus_AA, 1.2, 0.1), # Locus: AA, Fitness: 1.2
        (locus_Aa, 1.5, 0.5), # Locus: Aa, Fitness: 1.5
        (locus_bb, 0.2, 0.4), # Locus: bb, Fitness: 0.2
    ]
    
    ind_good = Individual(sex='F', genotype=genotype_good, fitness=1.0)
    ind_bad = Individual(sex='M', genotype=genotype_bad, fitness=1.0)
    
    ind_good.update_fitness(genepool_py)
    expected_fitness_good = 1.5 * (1.0 - 0.0005 * 1)
    assert abs(ind_good.fitness - expected_fitness_good) < 1e-6, "O fitness deve ser calculado corretamente (1.5)."
    
    locus_Cc = Locus(["C", "c"])
    genotype_error = Genotype(size=1)
    genotype_error.append(locus_Cc)
    ind_error = Individual(sex='F', genotype=genotype_error)
    
    try:
        ind_error.update_fitness(genepool_py)
        assert False, "update_fitness deveria falhar para Locus não encontrado."
    except ValueError as e:
        assert "Locus 'Cc' not found" in str(e), "A exceção deve indicar o Locus ausente."
        
# Execute com: pytest test_rust_bindings.py
