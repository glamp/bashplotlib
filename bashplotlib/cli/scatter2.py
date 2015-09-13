#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""scatter2 

Usage:
    scatter2 [[FILE|-f FILENAME] -t TITLE -b BINS -s SIZE -p MARKERSHAPE -x XLAB -c COLOUR] [-n] [-h]

Arguments:
    FILE                              Csv with 2 columns for x and y [default: ]
    -f --file FILENAME                Same as FILE but shorter and less explicit [default: ]
    -t --title TITLE                  Title for the chart [default: ]
    -X --X-vals X                     X values
    -y --y-vals y                     y values
    -s --size SIZE                    Height of the histogram in lines [default: 20.0]
    -p --pch MARKERSHAPE              Shape of each bar [default: x]
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
from bashplotlib.utils.helpers import try_cast_str_to_number

def _read_csv(filename, X=0, y=1, sep=',', header=False):
    X_y_pairs = []
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    if not data:
        return None
    else:
        if isinstance(X, int) and isinstance(y, int):
            X_idx, y_idx = X, y
        elif isinstance(X, basestring) and isinstance(y, basestring):
            if X.strip().isdigit() and y.strip().isdigit():
                X_idx, y_idx = map(try_cast_str_to_number, [X_idx, y_idx])
        else:
            X_idx, y_idx = None, None
        for i, line in enumerate(data):
            row = [item.strip() for item in line.strip().split(sep)]
            if i == 0:
                if header:
                    for j, col in enumerate(row):
                        if col.lower() == X.lower():
                            X_idx = j
                        if col.lower() == y.lower():
                            y_idx = j
                        if X_idx and y_idx:
                            continue
            if row and isinstance(row, list) and len(row):
                try:
                    X_value, y_value = row[X_idx], row[y_idx]
                    X_value, y_value = map(try_cast_str_to_number, [X_value, y_value])
                    X_y_pairs.append([X_value, y_value])
                except Exception, err:
                    continue
        return X_y_pairs


# # plot_scatter(opts.f, opts.x, opts.y, opts.size, opts.pch, opts.colour, opts.t)
# def parse_args():
#     """takes __doc__ for given cmd. Returns parsed args using docopt.
#     """
#     args = docopt()
#     for k, v in args.iteritems():
#         if v == 'None':
#             args[k] = None
#     if args['FILE'] and args['FILE'] != args['--file']:
#         args['--file'] = args['FILE']
#     if args['--file'] == 'stdin':
#         args['--file'] = read_stdin_or_timeout()
#         if args['--file'] is None:
#             print 
#             sys.exit(1)
#     plot_params = {
#         'bincount': args['--bins'],
#         'colour': args['--colour'],
#         'data': args['--file'],
#         'height': float(args['--height'].strip()),
#         'pch': args['--pch'],
#         'showSummary': (not args['--nosummary']),
#         'title': args['--title'],
#         'xlab': args['--xlab']
#     }
#     return plot_params
