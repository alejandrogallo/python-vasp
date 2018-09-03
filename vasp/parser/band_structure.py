import vasp.utils
import vasp.parser.regex
from vasp.parser.kpoint import Kpoint

# TODO: Spin polarized

class BandStructure:

    def __init__(self, outcar):
        self.kpoints = []
        with open(outcar) as fd:
            self.lines = fd.readlines()
        self.parse()

    def parse(self):
        self.lines = vasp.utils.clean_lines(self.lines)

        kpoint_lines = []
        kpoint_header_matched_before = False
        for line in self.lines:

            m = vasp.parser.regex.kpoint_header.match(line)
            if m:
                if kpoint_lines and kpoint_header_matched_before:
                    self.kpoints.append(Kpoint(kpoint_lines))
                kpoint_header_matched_before = True
                kpoint_lines = []

            m = vasp.parser.regex.end_section.match(line)
            if m:
                if kpoint_lines and kpoint_header_matched_before:
                    self.kpoints.append(Kpoint(kpoint_lines))
                kpoint_lines = []
                kpoint_header_matched_before = False

            kpoint_lines.append(line)
