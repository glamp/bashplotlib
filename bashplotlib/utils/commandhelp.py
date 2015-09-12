#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""commandhelp.py
"""
import sys
import os
from docopt import docopt
from bashplotlib.utils.helpers import *
from select import select

HIST_DOCSTRING = """hist - construct a histogram for a continuous variable from your terminal

Usage:
    hist [[FILE | -f FILENAME] -t TITLE -b BINS -s SIZE -p MARKERSHAPE -x XLAB -c COLOUR] [-n] [-h]

Arguments:
    FILE                              A file containing a column of numbers [default: stdin]
    -f --file FILENAME                Same as FILE but shorter and less explicit [default: stdin]
    -t --title TITLE                  Title for the chart [default: ]
    -b --bins BINS                    Number of bins in the histogram [default: None]
    -s --height SIZE                  Height of the histogram in lines [default: 20.0]
    -p --pch MARKERSHAPE              Shape of each bar [default: o]
    -x --xlab XLAB                    Label bins on x-axis [default: None]
    -c --colour COLOUR                Colour of the plot (Pink, blue, green, red, white, aqua, grey, yellow) [default: white]

Options:
    -n --nosummary                    Hide summary
    -h --help                         Show this screen

Examples:
    $ hist test.csv -t "you're the man now dog"
    $ hist -f test.csv -t "you're the man now dog"
    $ hist --file test.csv -t "you're the man now dog"
    $ cat test.csv | hist -t "you're the man now dog"

"""

# SCATTER_DOCSTRING = """scatter - construct a scatter plot from your terminal

# Usage:
#     scatter [[FILE | -f FILENAME] -t TITLE -b BINS -s SIZE -p MARKERSHAPE -x XLAB -c COLOUR] [-n] [-h]


# """

scatter = {
    "usage": """scatterplot is a command for making xy plots. it accepts a series of x values and a series of y values in the 
    following formats:
        1) a txt file or standard in value w/ 2 comma seperated columns of x,y values
        2) 2 txt files. 1 w/ designated x values and another with designated y values.
    
    scatter -x <xcoords> -y <ycoords>
    cat <file_with_x_and_y_coords> | scatter

    """
}

def _read_stdin_or_timeout():
    timeout = 0.5
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        return sys.stdin.readlines()
    else:
        return None

def parse_args(command_docstring):
    """takes __doc__ for given cmd. Returns parsed args using docopt.
    """
    args = docopt(command_docstring)
    for k, v in args.iteritems():
        if v == 'None':
            args[k] = None
    if args['FILE'] and args['FILE'] != args['--file']:
        args['--file'] = args['FILE']
    if args['--file'] == 'stdin':
        args['--file'] = _read_stdin_or_timeout()
        if args['--file'] is None:
            print command_docstring
            sys.exit(1)
    plot_params = {
        'bincount': args['--bins'],
        'colour': args['--colour'],
        'f': args['--file'],
        'height': float(args['--height'].strip()),
        'pch': args['--pch'],
        'showSummary': (not args['--nosummary']),
        'title': args['--title'],
        'xlab': args['--xlab']
    }
    return plot_params
