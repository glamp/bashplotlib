#!/usr/bin/evn python
# -*- coding: utf-8 -*-

"""
Various helpful function for bashplotlib
"""

import sys

isiterable = lambda x: hasattr(x, '__iter__') or hasattr(x, '__getitem__')

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


def get_colour(colour, default="default"):
    """
    Get the escape code sequence for a colour
    """
    return bcolours.get(colour, bcolours[default])


def printcolour(text, sameline=False, colour="default"):
    """
    Print color text using escape codes
    """
    sep = '' if sameline else '\n'

    # If no colour set, do not print color ESC characters
    if get_colour(colour) == get_colour("ENDC"):
        sys.stdout.write(text + sep)
    else:
        sys.stdout.write(get_colour(colour) + text + get_colour("ENDC") + sep)


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


def abbreviate(labels, rfill=' '):
    """
    Abbreviate labels without introducing ambiguities.
    """
    max_len = max(len(l) for l in labels)
    for i in range(1, max_len):
        abbrev = [l[:i].ljust(i, rfill) for l in labels]
        if len(abbrev) == len(set(abbrev)):
            break
    return abbrev


def box_text(text, width, offset=0):
    """
    Return text inside an ascii textbox
    """
    box = " " * offset + "-" * (width+2) + "\n"
    box += " " * offset + "|" + text.center(width) + "|" + "\n"
    box += " " * offset + "-" * (width+2)
    return box
