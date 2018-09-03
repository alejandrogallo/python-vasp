import re


class BandStructure:
    def __init__(self, outcar):
        with open(outcar) as fd:
            self.outcar_lines = outcar.readlines()
