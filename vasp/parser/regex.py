"""
Collections of regular expressions to be shared by different module
"""
import re


band = re.compile(r'^(\d+) ([^ ]+) ([^ ]+)$')
band_header = re.compile(r"^band No. band energies occupation$")
kpoint_header = re.compile(r"^k-point (\d+) : ([^ ]+) ([^ ]+) ([^ ]+)$")
spin_component_header = re.compile(r"^spin component ([12])$")

# This is for the outcar, every section seems to end by a long series of '-'
end_section = re.compile(r'-' * 30)

vector = re.compile(
    r'^ *(\+?-?\d.?\d*E?\+?-?\d*) *'
    r'(\+?-?\d.?\d*E?\+?-?\d*) *'
    r'(\+?-?\d.?\d*E?\+?-?\d*) *$'
)


def parse_vector(line):
    m = vector.match(line)
    if not m:
        raise SyntaxError(
            'Line "{0}" does not seem to be a vector'.format(line)
        )
    else:
        return [float(m.group(i + 1)) for i in range(3)]
