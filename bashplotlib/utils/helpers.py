# -*- coding: utf-8 -*-

"""
Various helpful function for bashplotlib
"""
from __future__ import print_function
import sys

isiterable = lambda x: hasattr(x, '__iter__') or hasattr(x, '__getitem__')

bcolours = {
    "white": '\033[97m',
    "aqua": '\033[96m',
    "pink": '\033[95m',
    "blue": '\033[94m',
    "yellow": '\033[93m',
    "green": '\033[92m',
    "red": '\033[91m',
    "grey": '\033[90m',
    "black": '\033[30m',
    "default": '\033[39m',
    "ENDC": '\033[39m',
}

colour_help = ', '.join([colour for colour in bcolours if colour != "ENDC"])


def get_colour(colour):
    """
    Get the escape code sequence for a colour
    """
    return bcolours.get(colour, bcolours['ENDC'])

def print_return_str(text, end='\n', return_str=False):
    if not return_str:
        print(text, end=end)
    return text + end

def printcolour(text, sameline=False, colour=get_colour("ENDC"), return_str=False):
    """
    Print color text using escape codes
    """
    if sameline:
        sep = ''
    else:
        sep = '\n'
    if colour == 'default' or colour == 'ENDC' or colour is None:
        return print_return_str(text, sep, return_str)
    return print_return_str(get_colour(colour) + text + bcolours["ENDC"],
                            sep, return_str)

def drange(start, stop, step=1.0, include_stop=False):
    """
    Generate between 2 numbers w/ optional step, optionally include upper bound
    """
    if step == 0:
        step = 0.01
    r = start

    if include_stop:
        while r <= stop:
            yield r
            r += step
            r = round(r, 10)
    else:
        while r < stop:
            yield r
            r += step
            r = round(r, 10)


def box_text(text, width, offset=0):
    """
    Return text inside an ascii textbox
    """
    box = " " * offset + "-" * (width + 2) + "\n"
    box += " " * offset + "|" + text.center(width) + "|" + "\n"
    box += " " * offset + "-" * (width + 2)
    return box
