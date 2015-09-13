#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""utils/helpers.py
"""
import os, sys

bcolours = {
    "white": '\033[97m',
    "aqua": '\033[96m',
    "pink": '\033[95m',
    "blue": '\033[94m',
    "yellow": '\033[93m',
    "green": '\033[92m',
    "red": '\033[91m',
    "grey": '\033[90m',
    "ENDC": '\033[0m'
}

def get_colour(colour):
    return bcolours.get(colour, bcolours['white'])

def printcolor(txt, sameline=False, color=get_colour("white")):
    if sameline:
        if color=='\033[97m':
            print txt,
        else:
            print color + txt + bcolours["ENDC"],
    else:
        if color=='\033[97m':
            print txt
        else:
            print color + txt + bcolours["ENDC"]

def drange(start, stop, step=1.0):
    "generate between 2 numbers w/ optional step"
    if step==0:
        step = 0.01
    r = start
    while r < stop:
        yield r
        r += step

def box_text(text, width, offset=0):
    box = " "*offset + "-"*(width+2) + "\n"
    box += " "*offset + "|"+ text.center(width) + "|" + "\n"
    box += " "*offset + "-"*(width+2)
    return box

def try_cast_str_to_number(number_str, verbose=False):
    "takes txt and tries to coerce it to float"
    try:
        return float(number_str.strip())
    except Exception, err:
        if verbose:
            sys.stderr.write(err.message)
            sys.stderr.flush()
        return None
