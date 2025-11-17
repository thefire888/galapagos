from galapagos.locus import Locus

def test_equals_to():
    locus_a = Locus(("A", "a"))
    locus_b = Locus(("a", "A"))
    assert locus_a == locus_b
    assert locus_b == locus_a

