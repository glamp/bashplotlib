#!/usr/bin/python
import math
import optparse
import sys
from utils.helpers import *
from utils.commandhelp import hist

def calc_bins(n, min_val, max_val, h=None):
    "calculate number of bins for the histogram"
    if not h:
        h = max(10, math.log(n + 1, 2)) 
    bin_width = (max_val - min_val) / h
    for b in drange(min_val, max_val, bin_width):
        yield b

def read_numbers(numbers):
    "read the input data in the most optimal way"
    if isinstance(numbers, list):
        for n in numbers:
            n = str(n)
            yield float(n.strip())
    else:
        for n in open(numbers):
            yield float(n.strip())

def run_demo():
    "demo the product"
    #plotting a histogram
    print "plotting a basic histogram"
    print "plot_hist('./data/exp.txt')"
    print "hist -f ./data/exp.txt"
    print "cat ./data/exp.txt | hist"
    plot_hist('./data/exp.txt')
    print "*"*80
    #with colors
    print "histogram with colors"
    print "plot_hist('./data/exp.txt', colour='blue')"
    print "hist -f ./data/exp.txt -c blue"
    plot_hist('./data/exp.txt', colour='blue')
    print "*"*80
    #changing the shape of the point
    print "changing the shape of the bars"
    print "plot_hist('./data/exp.txt', pch='.')"
    print "hist -f ./data/exp.txt -p ."
    plot_hist('./data/exp.txt', pch='.')
    print "*"*80
    #chagning the size of the plot
    print "chagning the size of the plot"
    print "plot_hist('./data/exp.txt', height=35.0, bincount=40)"
    print "hist -f ./data/exp.txt -s 35.0 -b 40"
    plot_hist('./data/exp.txt', height=35.0, bincount=40)

def plot_hist(f, height=20.0, bincount=None, pch="o", colour="white", title="", xlab=None, showSummary=False):
    """make a histogram

        Keyword arguments:
        height -- the height of the histogram in # of lines
        bincount -- number of bins in the histogram
        pch -- shape of the bars in the plot
        colour -- colour of the bars in the terminal
        title -- title at the top of the plot
        xlab -- boolen value for whether or not to display x-axis labels
        showSummary -- boolean value for whether or not to display a summary
    """
    
    if pch is None:
        pch = "o"
    
    colour = get_colour(colour)

    min_val, max_val = None, None
    n, mean = 0., 0.
    for number in read_numbers(f):
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
    for number in read_numbers(f):
        for i, b in enumerate(bins):
            if number < b:
                hist[i] += 1
                break

    min_y, max_y = min(hist.values()), max(hist.values())
  
    ys = list(drange(min_y, max_y, (max_y-min_y)/height))
    ys.reverse()
    
    nlen = max(len(str(min_y)), len(str(max_y))) + 1
    
    if title:
        print box_text(title, len(hist)*2, nlen)
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
                printcolor(pch, True, colour)
            else:
                printcolor(" ", True, colour)
        print
    xs = hist.keys() * 2

    print " "*(nlen+1) + "-"*len(xs)


    if xlab:
        for i in range(0, nlen):
            printcolor(" "*(nlen+1), True, colour)
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


if __name__=="__main__":

    parser = optparse.OptionParser(usage=hist['usage'])

    parser.add_option('-f', '--file', help='a file containing a column of numbers',
                      default=None, dest='f')
    parser.add_option('-t', '--title', help='title for the chart',
                      default="", dest='t')
    parser.add_option('-b', '--bins', help='number of bins in the histogram',
                      type='int', default=None, dest='b')
    parser.add_option('-s', '--height', help='height of the histogram (in lines)',
                      type='int', default=20., dest='h')
    parser.add_option('-p', '--pch', help='shape of each bar', default='o', dest='p')
    parser.add_option('-x', '--xlab', help='label bins on x-axis', default=None, action="store_true", dest='x')
    parser.add_option('-c', '--colour', help='colour of the plot (%s)' % ", ".join([c for c in bcolours.keys() if c != 'ENDC']),
                      default='white', dest='colour')
    parser.add_option('-d', '--demo', help='run demos', action='store_true', dest='demo')
    parser.add_option('-n', '--nosummary', help='hide summary', action='store_false', dest='showSummary', default=True)

    (opts, args) = parser.parse_args()

    if opts.f is None:
        if len(args) > 0:
            opts.f = args[0]
        elif opts.demo is False:
            opts.f = sys.stdin.readlines()

    if opts.demo:
        run_demo()
    elif opts.f:
        plot_hist(opts.f, opts.h, opts.b, opts.p, opts.colour, opts.t, opts.x, opts.showSummary)
    else:
        print "nothing to plot!"

