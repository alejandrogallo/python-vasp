import vasp.parser


def test_defs():
    assert(vasp.parser.BandStructure)
    assert(vasp.parser.Kpoint)
    assert(vasp.parser.Poscar)
