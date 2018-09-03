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
