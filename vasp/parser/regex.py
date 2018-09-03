"""
Collections of regular expressions to be shared by different modules
"""
import re


band = re.compile(r'(\d+) ([^ ]+) ([^ ]+)')
band_header = re.compile(r"band No. band energies occupation")
kpoint_header = re.compile(r"k-point (\d+) : ([^ ]+) ([^ ]+) ([^ ]+)")
