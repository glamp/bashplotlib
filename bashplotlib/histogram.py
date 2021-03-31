#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Plotting terminal based histograms
"""

from __future__ import print_function
from __future__ import division

import os
import sys
import math
import optparse
from os.path import dirname
from .utils.helpers import *
from .utils.commandhelp import hist


def calc_bins(n, min_val, max_val, h=None, binwidth=None):
    """
    Calculate number of bins for the histogram
    """
    if not h:
        h = max(10, math.log(n + 1, 2))
    if binwidth == 0:
        binwidth = 0.1
    if binwidth is None:
        binwidth = (max_val - min_val) / h
    for b in drange(min_val, max_val, step=binwidth, include_stop=True):
        if b.is_integer():
            yield int(b)
        else:
            yield b


def read_numbers(numbers):
    """
    Read the input data in the most optimal way
    """
    if isiterable(numbers):
        for number in numbers:
            yield float(str(number).strip())
    else:
        with open(numbers) as fh:
            for number in fh:
                yield float(number.strip())


def run_demo():
    """
    Run a demonstration
    """
    module_dir = dirname(dirname(os.path.realpath(__file__)))
    demo_file = os.path.join(module_dir, 'examples/data/exp.txt')

    if not os.path.isfile(demo_file):
        sys.stderr.write("demo input file not found!\n")
        sys.stderr.write("run the downloaddata.sh script in the example first\n")
        sys.exit(1)

    # plotting a histogram
    print("plotting a basic histogram")
    print("plot_hist('%s')" % demo_file)
    print("hist -f %s" % demo_file)
    print("cat %s | hist" % demo_file)
    plot_hist(demo_file)
    print("*" * 80)

    # with colours
    print("histogram with colours")
    print("plot_hist('%s', colour='blue')" % demo_file)
    print("hist -f %s -c blue" % demo_file)
    plot_hist(demo_file, colour='blue')
    print("*" * 80)

    # changing the shape of the point
    print("changing the shape of the bars")
    print("plot_hist('%s', pch='.')" % demo_file)
    print("hist -f %s -p ." % demo_file)
    plot_hist(demo_file, pch='.')
    print("*" * 80)

    # changing the size of the plot
    print("changing the size of the plot")
    print("plot_hist('%s', height=35.0, bincount=40)" % demo_file)
    print("hist -f %s -s 35.0 -b 40" % demo_file)
    plot_hist(demo_file, height=35.0, bincount=40)


def plot_hist(f, height=20.0, bincount=None, binwidth=None, pch="o", colour="default", title="", xlab=None, showSummary=False, regular=False):
    """
    Make a histogram

    Arguments:
        height -- the height of the histogram in # of lines
        bincount -- number of bins in the histogram
        binwidth -- width of bins in the histogram
        pch -- shape of the bars in the plot
        colour -- colour of the bars in the terminal
        title -- title at the top of the plot
        xlab -- boolean value for whether or not to display x-axis labels
        showSummary -- boolean value for whether or not to display a summary
        regular -- boolean value for whether or not to start y-labels at 0
    """
    if pch is None:
        pch = "o"

    if isinstance(f, str):
        with open(f) as fh:
            f = fh.readlines()

    min_val, max_val = None, None
    n, mean, sd = 0.0, 0.0, 0.0

    for number in read_numbers(f):
        n += 1
        if min_val is None or number < min_val:
            min_val = number
        if max_val is None or number > max_val:
            max_val = number
        mean += number

    mean /= n

    for number in read_numbers(f):
        sd += (mean - number)**2

    sd /= (n - 1)
    sd **= 0.5

    bins = list(calc_bins(n, min_val, max_val, bincount, binwidth))
    hist = dict((i, 0) for i in range(len(bins)))

    for number in read_numbers(f):
        for i, b in enumerate(bins):
            if number <= b:
                hist[i] += 1
                break
        if number == max_val and max_val > bins[len(bins) - 1]:
            hist[len(hist) - 1] += 1

    min_y, max_y = min(hist.values()), max(hist.values())

    start = max(min_y, 1)
    stop = max_y + 1

    if regular:
        start = 1

    if height is None:
        height = stop - start
        if height > 20:
            height = 20

    ys = list(drange(start, stop, float(stop - start) / height))
    ys.reverse()

    nlen = max(len(str(min_y)), len(str(max_y))) + 1

    if title:
        print(box_text(title, max(len(hist) * 2, len(title)), nlen))
    print()

    used_labs = set()
    for y in ys:
        ylab = str(int(y))
        if ylab in used_labs:
            ylab = ""
        else:
            used_labs.add(ylab)
        ylab = " " * (nlen - len(ylab)) + ylab + "|"

        print(ylab, end=' ')

        for i in range(len(hist)):
            if int(y) <= hist[i]:
                printcolour(pch, True, colour)
            else:
                printcolour(" ", True, colour)
        print('')
    xs = hist.keys()

    print(" " * (nlen + 1) + "-" * len(xs))

    if xlab:
        labels = abbreviate([str(b) for b in bins])
        xlen = len(labels[0])
        for i in range(0, xlen):
            printcolour(" " * (nlen + 1), True, colour)
            for x in range(0, len(hist)):
                num = labels[x]
                if x % 2 != 0:
                    pass
                elif i < len(num):
                    print(num[i], end=' ')
                else:
                    print(" ", end=' ')
            print('')

    center = max(map(len, map(str, [n, min_val, mean, max_val])))
    center += 15

    if showSummary:
        print()
        print("-" * (2 + center))
        print("|" + "Summary".center(center) + "|")
        print("-" * (2 + center))
        summary = "|" + ("observations: %d" % n).center(center) + "|\n"
        summary += "|" + ("min value: %f" % min_val).center(center) + "|\n"
        summary += "|" + ("mean : %f" % mean).center(center) + "|\n"
        summary += "|" + ("std dev : %f" % sd).center(center) + "|\n"
        summary += "|" + ("max value: %f" % max_val).center(center) + "|\n"
        summary += "-" * (2 + center)
        print(summary)


def main():

    parser = optparse.OptionParser(usage=hist['usage'])

    parser.add_option(
        '-f', '--file', help='a file containing a column of numbers', default=None, dest='f')
    parser.add_option('-t', '--title', help='title for the chart', default="", dest='t')
    parser.add_option(
        '-b', '--bins', help='number of bins in the histogram', type='int', default=None, dest='b')
    parser.add_option('-w', '--binwidth', help='width of bins in the histogram',
                      type='float', default=None, dest='binwidth')
    parser.add_option('-s', '--height', help='height of the histogram (in lines)',
                      type='int', default=None, dest='h')
    parser.add_option('-p', '--pch', help='shape of each bar', default='o', dest='p')
    parser.add_option('-x', '--xlab', help='label bins on x-axis',
                      default=None, action="store_true", dest='x')
    parser.add_option('-c', '--colour', help='colour of the plot (%s)' %
                      colour_help, default='default', dest='colour')
    parser.add_option('-d', '--demo', help='run demos', action='store_true', dest='demo')
    parser.add_option('-n', '--nosummary', help='hide summary',
                      action='store_false', dest='showSummary', default=True)
    parser.add_option('-r', '--regular',
                      help='use regular y-scale (0 - maximum y value), instead of truncated y-scale (minimum y-value - maximum y-value)',
                      default=False, action="store_true", dest='regular')

    opts, args = parser.parse_args()

    if opts.f is None:
        if len(args) > 0:
            opts.f = args[0]
        elif opts.demo is None or opts.demo is False:
            opts.f = sys.stdin.readlines()

    if opts.demo:
        run_demo()
    elif opts.f:
        plot_hist(opts.f, opts.h, opts.b, opts.binwidth, opts.p, opts.colour,
                  opts.t, opts.x, opts.showSummary, opts.regular)
    else:
        print("nothing to plot!")


if __name__ == "__main__":
    main()
