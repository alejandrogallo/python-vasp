from vasp.parser.regex import *


def test_parse_vector():
    assert(parse_vector("  1 2    4", 3, float) == [1.0, 2.0, 4.0])
    assert(parse_vector("1 2 4", 3, float) == [1.0, 2.0, 4.0])
    assert(parse_vector("1.342 2 4.2", 3, float) == [1.342, 2.0, 4.2])
    assert(parse_vector(" -1.342 2 4.2", 3, float) == [-1.342, 2.0, 4.2])
    assert(parse_vector(" -1.342 2E2 4.2", 3, float) == [-1.342, 200.0, 4.2])
    assert(parse_vector(" -1.342 2e+2 4.2", 3, float) == [-1.342, 200.0, 4.2])
    assert(parse_vector(" -1.342 2e-2 4.2", 3, float) == [-1.342, 0.02, 4.2])

    try:
        assert(parse_vector("1.342 4.2", 3, float) == [1.342, 2.0, 4.2])
    except SyntaxError:
        assert(True)
    else:
        assert(False)

    try:
        assert(parse_vector("hello world", 3, float) == [1])
    except SyntaxError:
        assert(True)
    else:
        assert(False)

    assert(parse_vector(" -1 2 4", 3, int) == [-1, 2, 4])
