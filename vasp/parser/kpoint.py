from collections import namedtuple
import re

Band = namedtuple('Band', ['number', 'energy', 'occupation'])

class Kpoint:
    def __init__(self, lines):
        """

         k-point     1 :       0.5000    0.5000    0.5000
          band No.  band energies     occupation 
              1      -4.1306      2.00000
              2      -1.4815      2.00000
              3       4.2930      2.00000
              4       4.2930      2.00000
              5       7.0479      0.00000
              6       8.8314      0.00000
              7       8.8314      0.00000
              8      13.2218      0.00000

        :param lines: Lines containing an outcar kpoint
        :type  lines: list
        """
        self.lines = lines
        self.value = None
        self.index = None
        self.bands = []
        self.parse()

    def parse(self):

        # kill newlines
        self.lines = map(lambda x: x.replace("\n", ''), self.lines)

        # double spaces out
        self.lines = map(lambda x: re.sub(r'  *', ' ', x), self.lines)

        # Whitespaces at the begginning and end
        self.lines = map(lambda x: re.sub(r'^ *', '', x), self.lines)
        self.lines = map(lambda x: re.sub(r' *$', '', x), self.lines)

        # Whitespaces lines
        self.lines = map(lambda x: re.sub(r'^ *$', '', x), self.lines)

        # takeout empty lines
        self.lines = list(filter(lambda x: x, self.lines))

        header = self.lines[0]
        m = re.match(r"k-point (\d+) : ([^ ]+) ([^ ]+) ([^ ]+)", header)
        if not m:
            raise SyntaxError(
                'The header of the kpoint is not what is expected\n'
                'header = "{0}"'.format(header)
            )
        else:
            self.index = int(m.group(1))
            self.value = [float(m.group(i)) for i in range(2, 5)]

        legend = self.lines[1]
        m = re.match(r"band No. band energies occupation", legend)
        if not m:
            raise SyntaxError(
                'The legend of the kpoint is not what is expected\n'
                'legend = "{0}"'.format(legend)
            )

        # process bands
        bandregex = re.compile(r'(\d+) ([^ ]+) ([^ ]+)')
        for i in range(2, len(self.lines)):
            m = bandregex.match(self.lines[i])
            if not m:
                raise SyntaxError(
                    'Error parsing band, check it!\n'
                    'band = "{0}"'.format(self.lines[i])
                )
            self.bands.append(
                Band(
                    number=int(m.group(1)),
                    energy=float(m.group(2)),
                    occupation=float(m.group(3)),
                )
            )

