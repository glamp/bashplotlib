#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""scatter

Usage:
    scatter ((FILE | -f FILENAME) | (-X XDATA -y YDATA)) [-t TITLE -s SIZE -p MARKERSHAPE -c COLOUR] [-h -H]

Arguments:
    FILE                              Csv with 2 columns for x and y [default: ]
    -f --file FILENAME                Same as FILE but shorter and less explicit [default: ]
    -X --xs-file XDATA                Text file with 1 column for the X values [default: ]
    -y --ys-file YDATA                Text file with 1 column for the y values [default: ]
    -t --title TITLE                  Title for the chart [default: ]
    -s --size SIZE                    Height of the histogram in lines [default: 20.0]
    -p --pch MARKERSHAPE              Shape of each bar [default: x]
    -c --colour COLOUR                Colour of the plot (Pink, blue, green, red, white, aqua, grey, yellow) [default: white]
    -H --skip-header                  Skip the first row in FILENAME, XDATA, and YDATA [default: False] 

Options:
    -h --help                         Show this screen

Examples:
    $ scatter2 -X data/exp.txt -y data/exp.txt

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
    if args['--file'] is None and (args['--xs-file'] is None or args['--ys-file'] is None):
        print __doc__
        sys.exit(1)
    if args['FILE'] is not None or args['--file'] is not None:
        if args['FILE'] and args['FILE'] != args['--file']:
            args['--file'] = args['FILE']
        if args['--file'] == 'stdin':
            args['--file'] = read_stdin_or_timeout()
    plot_params = {
        'filename': args['--file'],
        'xs': args['--xs-file'],
        'ys': args['--ys-file'],
        'size': float(args['--size']),
        'pch': args['--pch'],
        'colour': args['--colour'],
        'title': args['--title'],
    }
    return {k: v for k,v in plot_params.items() if v is not None and v != ""}
