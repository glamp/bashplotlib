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
    if isinstance(numbers, list):
        for n in numbers:
            yield float(n.strip())
    else:
        for n in open(numbers):
            yield float(n.strip())

def plot_hist(f, height=20.0, bincount=None, pch="o", colour="white", title="", xlab=None):
    "plot a histogram given a file of numbers"
    #first apss
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
    hist = {i: 0 for i in range(len(bins))}
    for number in read_numbers(f):
        for i, b in enumerate(bins):
            if number < b:
                hist[i] += 1
                break

    min_y, max_y = min(hist.values()), max(hist.values())
  
    ys = list(drange(min_y, max_y, (max_y-min_y)/height))
    ys.reverse()
    
    nlen = max(len(str(min_y)), len(str(max_y))) + 1
    print title.center(len(hist) + nlen + 1)
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

    (opts, args) = parser.parse_args()
   
    if opts.f is None:
        if len(args) > 0:
            opts.f = args[0]
        else:
            opts.f = sys.stdin.readlines()

    if opts.f:
        plot_hist(opts.f, opts.h, opts.b, opts.p, opts.colour, opts.t, opts.x)
    else:
        print "nothing to plot!"

