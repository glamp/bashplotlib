# -*- coding: utf-8 -*-

"""
Plotting terminal based scatterplots
"""

from __future__ import print_function
import csv
import sys
import optparse
from os.path import isfile
from .utils.helpers import *
from .utils.commandhelp import scatter


def get_scale(series, is_y=False, steps=20):
    min_val = min(series)
    max_val = max(series)
    scaled_series = []
    for x in drange(min_val, max_val, (max_val - min_val) / steps,
                    include_stop=True):
        if x > 0 and scaled_series and max(scaled_series) < 0:
            scaled_series.append(0.0)
        scaled_series.append(x)

    if is_y:
        scaled_series.reverse()
    return scaled_series


def plot_scatter(xs, ys, size=None, pch='o',
                colour='red', title=None, return_str=False):
    ''' Scatter plot.
    ----------------------
    |                 *   |
    |               *     |
    |             *       |
    |           *         |
    |         *           |
    |        *            |
    |       *             |
    |      *              |
    -----------------------
    Parameters
    ----------
    xs : list, numpy.ndarray
        list of x series
    ys : list, numpy.ndarray
        list of y series
    size : int
        width of plot
    pch : str
        any character to represent a points
    colour : str, list(str)
        white,aqua,pink,blue,yellow,green,red,grey,black,default,ENDC
    title : str
        title for the plot, None = not show
    return_str : boolean
        return string represent the plot or print it out, default: False
    '''
    splot = ''
    plotted = set()
    cs = colour

    if size is None:
        size = 13

    if title:
        splot += print_return_str(
            box_text(title, 2 * len(get_scale(xs, False, size)) + 1),
            return_str=return_str)

    # ====== Top line ====== #
    splot += print_return_str(' ' + "-" * (len(get_scale(xs, False, size)) + 2),
                              return_str=return_str)
    # ====== Main plot ====== #
    for y in get_scale(ys, True, size):
        splot += print_return_str("|", end=' ', return_str=return_str)
        for x in get_scale(xs, False, size):
            point = " "
            for (i, (xp, yp)) in enumerate(zip(xs, ys)):
                if xp <= x and yp >= y and (xp, yp) not in plotted:
                    point = pch
                    plotted.add((xp, yp))
                    if isinstance(cs, list):
                        colour = cs[i]
            splot += printcolour(point, True, colour, return_str)
        splot += print_return_str(" |", return_str=return_str)
    # ====== Bottom line ====== #
    splot += print_return_str(' ' + "-" * (len(get_scale(xs, False, size)) + 2),
                              return_str=return_str)
    if return_str:
        return splot

def _plot_scatter(f, xs, ys, size, pch, colour, title):
    """
    Form a complex number.

    Arguments:
        f -- comma delimited file w/ x,y coordinates
        xs -- if f not specified this is a file w/ x coordinates
        ys -- if f not specified this is a filew / y coordinates
        size -- size of the plot
        pch -- shape of the points (any character)
        colour -- colour of the points
        title -- title of the plot
    """

    if f:
        if isinstance(f, str):
            f = open(f)

        data = [tuple(line.strip().split(',')) for line in f]
        xs = [float(i[0]) for i in data]
        ys = [float(i[1]) for i in data]
        if len(data[0]) > 2:
            cs = [i[2].strip() for i in data]
        else:
            cs = None
    else:
        xs = [float(str(row).strip()) for row in open(xs)]
        ys = [float(str(row).strip()) for row in open(ys)]
        if isfile(colour):
            cs = [str(row).strip() for row in open(colour)]
        else:
            cs = colour
    plot_scatter(xs, ys, size=size, pch=pch, colour=cs, title=title)

def main():

    parser = optparse.OptionParser(usage=scatter['usage'])

    parser.add_option('-f', '--file', help='a csv w/ x and y coordinates', default=None, dest='f')
    parser.add_option('-t', '--title', help='title for the chart', default="", dest='t')
    parser.add_option('-x', help='x coordinates', default=None, dest='x')
    parser.add_option('-y', help='y coordinates', default=None, dest='y')
    parser.add_option('-s', '--size', help='y coordinates', default=20, dest='size', type='int')
    parser.add_option('-p', '--pch', help='shape of point', default="x", dest='pch')
    parser.add_option('-c', '--colour', help='colour of the plot (%s)' %
                      colour_help, default='default', dest='colour')

    opts, args = parser.parse_args()

    if opts.f is None and (opts.x is None or opts.y is None):
        opts.f = sys.stdin.readlines()

    if opts.f or (opts.x and opts.y):
        _plot_scatter(opts.f, opts.x, opts.y, opts.size, opts.pch, opts.colour, opts.t)
    else:
        print("nothing to plot!")


if __name__ == "__main__":
    main()
