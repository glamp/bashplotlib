#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plotting terminal based scatterplots
"""

import csv
import sys
import optparse
from .utils.helpers import *
from .utils.commandhelp import scatter 


def get_scale(series, is_y=False, steps=20):
    min_val = min(series)
    max_val = max(series)
    scaled_series = []
    for x in drange(min_val, max_val, (max_val-min_val)/steps):
        if x > 0 and scaled_series and max(scaled_series) < 0:
            scaled_series.append(0.0)
        scaled_series.append(x)
    
    if is_y:
        scaled_series.reverse()
    return scaled_series


def plot_scatter(f, xs, ys, size, pch, colour, title):
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
        
        data = [tuple(map(float, line.strip().split(','))) for line in f]
        xs = [i[0] for i in data]
        ys = [i[1] for i in data]
    else:
        xs = [float(str(row).strip()) for row in open(xs)]
        ys = [float(str(row).strip()) for row in open(ys)]

    plotted = set()
    
    if title:
        print box_text(title, 2*len(get_scale(xs, False, size))+1)
    
    print "-" * (2*len(get_scale(xs, False, size))+2)
    for y in get_scale(ys, True, size):
        print "|",
        for x in get_scale(xs, False, size):
            point = " "
            for (i, (xp, yp)) in enumerate(zip(xs, ys)):
                if xp <= x and yp >= y and (xp, yp) not in plotted:
                    point = pch
                    #point = str(i) 
                    plotted.add((xp, yp))
            if x==0 and y==0:
                point = "o"
            elif x==0:
                point = "|"
            elif y==0:
                point = "-"
            printcolour(point, True, colour)
        print "|"
    print "-"*(2*len(get_scale(xs, False, size))+2)


def main():

    parser = optparse.OptionParser(usage=scatter['usage'])

    parser.add_option('-f', '--file', help='a csv w/ x and y coordinates', default=None, dest='f')
    parser.add_option('-t', '--title', help='title for the chart', default="", dest='t')
    parser.add_option('-x', help='x coordinates', default=None, dest='x')
    parser.add_option('-y', help='y coordinates', default=None, dest='y')
    parser.add_option('-s', '--size',help='y coordinates', default=20, dest='size', type='int')
    parser.add_option('-p', '--pch',help='shape of point', default="x", dest='pch') 
    parser.add_option('-c', '--colour', help='colour of the plot (%s)' % colour_help, default='default', dest='colour')

    opts, args = parser.parse_args()

    if opts.f is None and (opts.x is None or opts.y is None):
        opts.f = sys.stdin.readlines()

    if opts.f or (opts.x and opts.y):
        plot_scatter(opts.f, opts.x, opts.y, opts.size, opts.pch, opts.colour, opts.t)
    else:
        print "nothing to plot!"


if __name__=="__main__":
    main()
