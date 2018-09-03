from vasp.parser.kpoint import Kpoint


def test_basic_kpoint():
    data = [
     "                                                  \n",
     " k-point     123 :       0.5000    0.5000    0.5000 \n",
     " band No.  band energies     occupation           \n",
     " 1      -4.1306e2      2.00000                      \n",
     " 2      -1.4815      2.00000                      \n",
     " 3       4.2930      2.00000                      \n",
     " 4       4.2930      2.00000                      \n",
     " 5       7.0479      0.00000                      \n",
     " 6       8.8314      0.00000                      \n",
     " 7       8.8314      0.00000                      \n",
     "                                                  \n",
     " 8      13.2218      0.00000                      \n",
     "                                                  \n",
    ]
    kpoint = Kpoint(data)

    # newlines
    for line in kpoint.lines:
        assert(not line.endswith('\n'))

    assert(len(kpoint.lines) == 10)
    assert(kpoint.index == 123)
    assert(len(kpoint.value) == 3)
    assert(kpoint.value[0] == 0.5)
    assert(kpoint.value[1] == 0.5)
    assert(kpoint.value[2] == 0.5)

    # bands
    assert(len(kpoint.bands) == 8)
    assert(kpoint.bands[0].spin == None)
    assert(kpoint.bands[0].number == 1)
    assert(kpoint.bands[0].energy == -4.1306e2)
    assert(kpoint.bands[-1].spin == None)
    assert(kpoint.bands[-1].number == 8)
    assert(kpoint.bands[-1].energy == 13.2218)


def test_bad_kpoint():
    data = [
     "                                                  \n",
     " k-point     123 ;       0.5000    0.5000    0.5000 \n",
     " band No.  band energies     occupation           \n",
     " 1      -4.1306e2      2.00000                      \n",
     "                                                  \n",
    ]
    try:
        kpoint = Kpoint(data)
    except SyntaxError:
        assert(True)
    else:
        assert(False)

    data = [
     "                                                  \n",
     " k-point     123 :       0.5000    0.5000    0.5000 \n",
     " band No   band energies     occupation           \n",
     " 1      -4.1306e2      2.00000                      \n",
     "                                                  \n",
    ]
    try:
        kpoint = Kpoint(data)
    except SyntaxError:
        assert(True)
    else:
        assert(False)

    data = [
     "                                                  \n",
     " k-point     123 :       0.5000    0.5000    0.5000 \n",
     " band No.  band energies     occupation           \n",
     " %      -4.1306e2      2.00000                      \n",
     "                                                  \n",
    ]
    try:
        kpoint = Kpoint(data)
    except SyntaxError:
        assert(True)
    else:
        assert(False)
