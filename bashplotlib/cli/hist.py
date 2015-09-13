#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""hist - construct a histogram for a continuous variable from your terminal

Usage:
    hist [[FILE|-f FILENAME] -t TITLE -b BINS -s SIZE -p MARKERSHAPE -x XLAB -c COLOUR] [-n] [-h]

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
from docopt import docopt
from bashplotlib.cli.helpers import read_stdin_or_timeout

def parse_args():
    """takes __doc__ for given cmd. Returns parsed args using docopt.
    """
    args = docopt(__doc__)
    for k, v in args.iteritems():
        if v == 'None':
            args[k] = None
    if args['FILE'] and args['FILE'] != args['--file']:
        args['--file'] = args['FILE']
    if args['--file'] == 'stdin':
        args['--file'] = read_stdin_or_timeout()
        if args['--file'] is None:
            print __doc__
            sys.exit(1)
    plot_params = {
        'bincount': args['--bins'],
        'colour': args['--colour'],
        'data': args['--file'],
        'height': float(args['--height'].strip()),
        'pch': args['--pch'],
        'showSummary': (not args['--nosummary']),
        'title': args['--title'],
        'xlab': args['--xlab']
    }
    return plot_params
