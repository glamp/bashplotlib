#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""scatterplot.py
"""
from __future__ import print_function
import sys
import os
from bashplotlib.core import helpers

def get_scale(series, is_y=False, steps=20):
    try:
        min_val = min(series)
        max_val = max(series)
        scaled_series = []
        for x in helpers.drange(min_val, max_val, (max_val-min_val)/steps):
            if x > 0 and scaled_series and max(scaled_series) < 0:
                scaled_series.append(0.0)
            scaled_series.append(x)
        if is_y:
            scaled_series.reverse()
        return scaled_series
    except Exception, err:
        print(err)
        # print(series)
        print(is_y)
        print(steps)

def plot_scatter(filename=None, xs=None, ys=None, size=20, pch='x', colour='white', title=None, skipheader=False):
    """plot (X,y) pairs from columns in a file or 2 separate files
    
        Arguments:
            xs                   List of values to use on X axis [default: None]
            ys                   List of values to use on y axis [default: None]
            filename             Name of a csv file [default: None]
            skipheader           Skip the first row [default: False]
            size                 Marketsize [default: 20]
            pch                  Markershape [default: x]
            colour               Marker colour [default: white]
            title                Title [default: ]

    """

    if filename:
        data = helpers.read_xy_pairs_from_csv(filename, X=0, y=1, header=skipheader)
        xs = [i[0] for i in data]
        ys = [i[1] for i in data]
    else:
        xs = [line.strip() for line in open(xs, 'r').readlines()]
        ys = [line.strip() for line in open(ys, 'r').readlines()]
        if skipheader:
            xs = xs[1:]
            ys = ys[1:]
        xs = map(float, xs)
        ys = map(float, ys)
    if (xs is None or ys is None):
        raise Exception("Missing `xs` or `ys` data.")
    plotted = set()
    if title:
        print(helpers.box_text(title, 2 * len(get_scale(xs, False, size)) + 1))

    print("-" * (2 * len(get_scale(xs, False, size)) + 2))
    for y in get_scale(ys, True, size):
        print("|", end=' ')
        for x in get_scale(xs, False, size):
            point = " "
            for (i, (xp, yp)) in enumerate(zip(xs, ys)):
                if xp <= x and yp >= y and (xp, yp) not in plotted:
                    point = pch
                    #point = str(i)
                    plotted.add((xp, yp))
            if x == 0 and y == 0:
                point = "o"
            elif x == 0:
                point = "|"
            elif y == 0:
                point = "-"
            helpers.printcolour(point, True, colour)
        print("|")
    print("-" * (2 * len(get_scale(xs, False, size)) + 2))
