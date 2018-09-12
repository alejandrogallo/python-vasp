import vasp.utils
from vasp.parser.regex import parse_vector, atom_header


class Poscar:

    def __init__(self, poscar_path):
        # Wether cartesian or direct
        self.modeline = None
        self.basis = []
        self.name = ""
        self.constant = None
        self.symbols = []
        self.symbols_number = []
        self.natoms = None
        self.coordinates = []

        with open(poscar_path) as fd:
            self.lines = fd.readlines()
        self.parse()

    def parse(self):

        self.lines = vasp.utils.clean_lines(self.lines)
        self.name = self.lines.pop(0)
        self.constant = float(self.lines.pop(0))
        self.basis.append(parse_vector(self.lines.pop(0), 3, float))
        self.basis.append(parse_vector(self.lines.pop(0), 3, float))
        self.basis.append(parse_vector(self.lines.pop(0), 3, float))

        self.symbols = atom_header.findall(self.lines.pop(0))
        if not self.symbols:
            raise SyntaxError(
                "There is no description of the atoms in the poscar\n"
                "Please write explicitly the atoms appearing in the poscar"
            )

        self.symbols_number = parse_vector(
            self.lines.pop(0), len(self.symbols), int
        )
        self.natoms = sum(self.symbols_number)

        self.modeline = self.lines.pop(0)

        for i in range(self.natoms):
            self.coordinates.append(parse_vector(self.lines.pop(0), 3, float))
