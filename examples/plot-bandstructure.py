#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from vasp.parser.band_structure import BandStructure
import click
import matplotlib.pyplot as plt


@click.command()
@click.help_option('-h', '--help')
@click.argument('outcar')
@click.option(
    '-t', '--title',
    help='Plot title',
    default=''
)
@click.option(
    '--xl', '--xlabel',
    help='x axis label',
    default=''
)
@click.option(
    '--yl', '--ylabel',
    help='y ayis label',
    default=''
)
@click.option(
    '--ls', '--line-style',
    help='Matplotlib style for the lines, default ".-"',
    default='.-'
)
@click.option(
    '--color-occupation',
    help='Color occupied and unnocupied bands differently',
    default=False,
    is_flag=True
)
@click.option(
    '-o', '--out',
    help='Output image',
    default=None,
)
def main(
        outcar, title, xlabel, ylabel,
        color_occupation, line_style, out
        ):
    """
    Plot band structure from an outcar file
    """
    bs = BandStructure(outcar)

    nbands = len(bs.kpoints[0].bands)
    kpoints = [k.index for k in bs.kpoints]
    bands = [[k.bands[i] for k in bs.kpoints] for i in range(nbands)]

    print('NBANDS   = {0}'.format(nbands))
    print('#KPOINTS = {0}'.format(len(kpoints)))

    for i in range(nbands):
        band = bands[i]
        occupation = sum(p.occupation for p in band) / len(band)
        if color_occupation:
            color = plt.get_cmap('RdBu')(occupation)
        else:
            color=None
        plt.plot(
            kpoints,
            [b.energy for b in band],
            line_style,
            color=color
        )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()

    if out:
        plt.savefig(out)

    plt.show()


if __name__ == "__main__":
    main()

#vim-run: python3 % OUTCAR -t 'Silicon bandstructure' --color-occupation
