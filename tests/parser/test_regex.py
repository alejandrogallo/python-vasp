from vasp.parser.regex import *


def test_parse_vector():
    assert(parse_vector("  -.342 -2e-2 4.2", None, float) == [-0.342, -0.02, 4.2])
    assert(parse_vector("  1 2    4", 3, float) == [1.0, 2.0, 4.0])
    assert(parse_vector("1 2 4", 3, float) == [1.0, 2.0, 4.0])
    assert(parse_vector("1.342 2 4.2", 3, float) == [1.342, 2.0, 4.2])
    assert(parse_vector(" -1.342 2 4.2", 3, float) == [-1.342, 2.0, 4.2])
    assert(parse_vector(" -1.342 2E2 4.2", 3, float) == [-1.342, 200.0, 4.2])
    assert(parse_vector(" -1.342 2e+2 4.2", 3, float) == [-1.342, 200.0, 4.2])
    assert(parse_vector(" -1.342 2e-2 4.2", 3, float) == [-1.342, 0.02, 4.2])
    assert(parse_vector(" -1.342 -2e-2 4.2", 3, float) == [-1.342, -0.02, 4.2])

    try:
        assert(parse_vector("1.342 4.2", 3, float) == [1.342, 2.0, 4.2])
    except IndexError:
        assert(True)
    else:
        assert(False)

    try:
        assert(parse_vector("hello world", 3, float) == [1])
    except ValueError:
        assert(True)
    else:
        assert(False)

    assert(parse_vector(" -1 2 4", 3, int) == [-1, 2, 4])

    assert(parse_vector(" -1 2 4", None, int) == [-1, 2, 4])

    line = (
        '13.567      12.386      9.4865      6.2601      3.8194      '
        '2.4781      1.9825      1.9538      2.0889      2.1838    '
    )
    parsed = parse_vector(line, None, float)
    assert(parsed[0] == 13.567)
