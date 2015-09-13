#!/usr/bin/python
import csv
import optparse
import sys
from bashplotlib.utils import helpers
from utils.commandhelp import scatter 


def get_scale(series, is_y=False, steps=20):
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

def plot_scatter(f, xs, ys, size, pch, colour, title):
    """Form a complex number.
    
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

    colour = helpers.get_colour(colour)

    plotted = set()
    
    if title:
        print helpers.box_text(title, 2*len(get_scale(xs, False, size))+1)
    
    print "-"*(2*len(get_scale(xs, False, size))+2)
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
            printcolor(point, True, colour)
        print "|"
    print "-"*(2*len(get_scale(xs, False, size))+2)


