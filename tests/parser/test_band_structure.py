from vasp.parser.band_structure import BandStructure
import os


def test_simple():
    outcarpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'data', 'outcar.1'
    )
    os.path.exists(outcarpath)

    bs = BandStructure(outcarpath)
    assert(bs is not None)

    empty_lines = list(filter(lambda x: not x, bs.lines))

    assert(not empty_lines)
    assert(isinstance(bs.kpoints, list))
    assert(len(bs.kpoints) == 40)

    for kpoint in bs.kpoints:
        assert(len(kpoint.bands) == 8)
        assert(kpoint.bands[-1].number == 8)
