import os
from vasp.parser.chgcar import Chgcar


def test_simple():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'parchg'
    )

    chgcar = Chgcar(path)
    assert(chgcar.poscar)
    assert(chgcar.poscar.name == 'Test chgcar')
    assert(chgcar.grid == [36, 36, 36])
    assert(chgcar.nvalues == 36 ** 3)
    assert(chgcar.values)
    assert(chgcar.values[0])
    assert(len(chgcar.values[0]) == 36 ** 3)
    assert(chgcar.values[0][0] == 13.567)
    assert(chgcar.values[0][-1] == 8.0069)


def test_simple_ispin2():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'parchg.ispin.2'
    )

    chgcar = Chgcar(path)
    assert(chgcar.poscar)
    assert(chgcar.poscar.name == 'Test chgcar')
    assert(chgcar.grid == [36, 36, 36])
    assert(chgcar.nvalues == 36 ** 3)

    assert(chgcar.values)
    assert(len(chgcar.values) == 2)

    assert(len(chgcar.values[0]) == 36 ** 3)
    assert(chgcar.values[0][0] == 13.567)
    assert(chgcar.values[0][-1] == 8.0069)

    assert(len(chgcar.values[1]) == 36 ** 3)
    assert(chgcar.values[1][0] == 11233.567)
    assert(chgcar.values[1][-1] == 123.0069)


def test_chgcar():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'CHGCAR'
    )

    chgcar = Chgcar(path)
    assert(chgcar.poscar)
    assert(chgcar.poscar.name == 'unknown system')
    assert(chgcar.grid == [10, 10, 10])
    assert(chgcar.nvalues == 10 ** 3)

    assert(chgcar.values)
    assert(len(chgcar.values) == 1)

    assert(len(chgcar.values[0]) == 10 ** 3)
    assert(chgcar.values[0][0] == 0.12243538616E+02)
    assert(chgcar.values[0][-1] == 0.64003393858E+02)
