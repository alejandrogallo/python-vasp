import os
from vasp.parser.poscar import *


def test_direct():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'poscar_simple_direct'
    )

    poscar = Poscar(path)
    assert(poscar.constant == -16.50931)
    assert(len(poscar.basis) == 3)

    assert(len(poscar.symbols) == 2)
    assert(poscar.symbols[0] == 'Li')
    assert(poscar.symbols[1] == 'Cl')

    assert(len(poscar.symbols_number) == 2)
    assert(poscar.symbols_number == [1, 1])

    assert(poscar.natoms == 2)

    assert(poscar.modeline == 'Direct')
    assert(len(poscar.coordinates) == 2)

