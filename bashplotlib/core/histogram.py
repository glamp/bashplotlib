#!/usr/bin/python
import math
import sys, os
from bashplotlib.utils import helpers
import collections

def calc_bins(n, min_val, max_val, h=None):
    "calculate number of bins for the histogram"
    if not h:
        h = max(10, math.log(n + 1, 2)) 
    bin_width = (max_val - min_val) / h
    for b in helpers.drange(min_val, max_val, bin_width):
        yield b

def read_numbers(numbers):
    "read input optimally; skip NA values. Takes a list() or a file."
    if not numbers:
        numbers = []
    if isinstance(numbers, basestring):
        try:
            # read numbers from file
            # ignore empty rows
            numbers = [line for line in open(numbers, 'r') if line.strip()] 
        except Exception, err:
            pass
    if isinstance(numbers, collections.Iterable):
        for number in numbers:
            number = helpers.try_cast_str_to_number(number)
            if number:
                yield number


def plot_hist(data, height=20.0, bincount=None, pch="o", colour="white", title="", xlab=None, showSummary=False):
    """make a histogram for continuous variable.

        Arguments:
            data:           List of numbers or file with numbers
            height:         The height of the histogram in # of lines
            bincount:       Number of bins in the histogram
            pch:            Shape of the bars in the plot
            colour:         Colour of the bars in the terminal
            title:          Title at the top of the plot
            xlab:           Boolen value for whether or not to display x-axis labels
            showSummary:    Boolean value for whether or not to display a summary
    """
    if pch is None:
        pch = "o"
    colour = helpers.get_colour(colour)
    min_val, max_val = None, None
    n, mean = 0., 0.
    for number in read_numbers(data):
        n += 1

        if not min_val or number < min_val:
            min_val = number
        if not max_val or number > max_val:
            max_val = number
        mean += number
    mean /= n

    bins = list(calc_bins(n, min_val, max_val, bincount))
    hist = {}
    for i in range(len(bins)):
        hist[i] = 0
    for number in read_numbers(data):
        for i, b in enumerate(bins):
            if number < b:
                hist[i] += 1
                break

    min_y, max_y = min(hist.values()), max(hist.values())
  
    ys = list(helpers.drange(min_y, max_y, (max_y-min_y)/height))
    ys.reverse()
    
    nlen = max(len(str(min_y)), len(str(max_y))) + 1
    
    if title:
        print helpers.box_text(title, len(hist)*2, nlen)
    print
    used_labs = set()
    for y in ys:
        ylab = str(int(y))
        if ylab in used_labs:
            ylab = ""
        else:
            used_labs.add(ylab)
        ylab = " "*(nlen - len(ylab)) + ylab + "|"

        print ylab,

        for i in range(len(hist)):
            if y < hist[i]:
                helpers.printcolor(pch, True, colour)
            else:
                helpers.printcolor(" ", True, colour)
        print
    xs = hist.keys() * 2

    print " "*(nlen+1) + "-"*len(xs)


    if xlab:
        for i in range(0, nlen):
            helpers.printcolor(" "*(nlen+1), True, colour)
            for x in range(0, len(hist)):
                num = str(bins[x])
                if x%2==0:
                    print " ",
                elif i < len(num):
                    print num[i],
            print
    center = max(map(len, map(str, [n, min_val, mean, max_val])))
    center += 15
    
    if showSummary:
        print
        print "-"*(2 + center)
        print "|" + "Summary".center(center) + "|"
        print "-"*(2 + center)
        summary = "|" + ("observations: %d" % n).center(center) + "|\n"
        summary += "|" + ("min value: %f" % min_val).center(center) + "|\n"
        summary += "|" + ("mean : %f" % mean).center(center) + "|\n"
        summary += "|" + ("max value: %f" % max_val).center(center) + "|\n"
        summary += "-"*(2 + center)
        print summary
