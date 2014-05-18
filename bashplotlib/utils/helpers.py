#!/usr/bin/evn python
# -*- coding: utf-8 -*-

"""
Various helpful function for bashplotlib
"""

import sys

bcolours = {
    "white":   '\033[97m',
    "aqua":    '\033[96m',
    "pink":    '\033[95m',
    "blue":    '\033[94m',
    "yellow":  '\033[93m',
    "green":   '\033[92m',
    "red":     '\033[91m',
    "grey":    '\033[90m',
    "black":   '\033[30m',
    "default": '\033[39m',
    "ENDC":    '\033[39m',
}

colour_help = ', '.join([colour for colour in bcolours if colour != "ENDC"])


def get_colour(colour):
    """
    Get the escape code sequence for a colour
    """
    return bcolours.get(colour, bcolours['ENDC'])


def printcolour(text, sameline=False, colour=get_colour("ENDC")):
    """
    Print color text using escape codes
    """
    if sameline:
        sep = ''
    else:
        sep = '\n'
    sys.stdout.write(get_colour(colour) + text + bcolours["ENDC"] + sep)


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
    box = " " * offset + "-" * (width+2) + "\n"
    box += " " * offset + "|" + text.center(width) + "|" + "\n"
    box += " " * offset + "-" * (width+2)
    return box
