from vasp.parser.band_structure import BandStructure
import os


def test_ispin_1():
    outcarpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'outcar.1'
    )
    assert(os.path.exists(outcarpath))

    bs = BandStructure(outcarpath)
    assert(bs is not None)

    empty_lines = list(filter(lambda x: not x, bs.lines))

    assert(not empty_lines)
    assert(isinstance(bs.kpoints, list))
    assert(len(bs.kpoints) == 40)

    for kpoint in bs.kpoints:
        assert(len(kpoint.bands) == 8)
        assert(kpoint.bands[-1].number == 8)


def test_ispin_2():
    outcarpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'outcar.ispin.2'
    )
    assert(os.path.exists(outcarpath))

    bs = BandStructure(outcarpath)
    assert(bs is not None)

    spin_1 = [k for k in bs.kpoints if k.bands[0].spin == 1]
    spin_2 = [k for k in bs.kpoints if k.bands[0].spin == 2]
    assert(spin_1 and spin_2)
    assert(len(spin_1) == len(spin_2))
