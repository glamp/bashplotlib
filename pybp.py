


plt = """
|            x
|          x
|        x
|      x
|    x
|  x  
|
|___________________
"""
import math

func = lambda x: int(math.sqrt(abs(x)))

def list_to_plot(aplt):
    aplt.reverse()
    fplt = []
    for row in aplt:
        fplt.append("".join(row))
    return "\n".join(fplt)

    # return "\n".join(["".join(row) for row in aplt])

def shapify(x, y):
    if x==max_x/2:
        return "|"
    elif y==max_y/2:
        return "-"
    else:
        return " "

# shapes = list("x.*+=#")
shapes = [u"\U0001F415", u"\U0001F355", u"\u2605", u"\u25CF", u"\u25D0"]

funcs = [
    lambda x: int(math.sqrt(abs(x))),
    lambda x: abs(x),
    # lambda x: x**2 - 5,
    lambda x: -x + 5,
]

max_x, max_y = 51, 51

plt = [[shapify(j, i) for j in range(max_x)] for i in range(max_y)]

for x in range(len(plt)):
    ix = x - max_x/2

    for shape, func in zip(shapes, funcs):
        iy = func(ix) + max_y/2
        if iy < len(plt):
            plt[iy][x] = shape
# print list_to_plot(plt)



print "\n"*5

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def calc_n_bins(points):
    return int(math.sqrt(len(points)))

def get_bins(n_bins, points):
    points = sorted(points)
    max_v, min_v = max(points), min(points)
    bin_width = (max_v - min_v) / float(n_bins)

    return bin_width, frange(min_v, max_v, bin_width)

def calc_widths(points, n_bins):
    counts = []
    bw, bins = get_bins(n_bins, points)
    for i in bins:
        counts.append(len([p for p in points if p>i and p<=i+bw]))
    return counts

import random

# data = [random.randint(-1000, 1000) for i in range(2000)]
# data = [random.normalvariate(100, 10) for i in range(2000)]
data = [random.expovariate(2.5) for i in range(2000)]
import sys

#data = [float(line.strip()) for line in sys.stdin.readlines()]

widths = calc_widths(data, calc_n_bins(data))


plt = [list("-"*w) for w in widths]

mw = max(widths)
y = [i for i in frange(0, mw, mw/50.0)]
y.reverse()
for i, ylab in enumerate(y):
    if i % 5 == 0:
        print str(int(ylab)).center(3),"  |",
    else:
        print str(" ").center(3),"  |",
    for p in widths:
        if p >= ylab:
            print u"\u25A1" + " ",
        else:
            print "  ",
    print

print "      " +  "---"*len(widths)

print "    ",
for i, bin in enumerate(get_bins(calc_n_bins(data), data)[1]):
    if i%3 <= 1:
        print ("%d" % bin).ljust(3),








