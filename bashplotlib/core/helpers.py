#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""core/helpers.py
"""
import os
import sys
import collections

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

def isiterable(obj):
    """
    Return True if you can loop over obj otherwise False
    """
    return isinstance(obj, collections.Iterable)

def get_colour(colour):
    return bcolours.get(colour, bcolours['white'])

def printcolour(text, sameline=False, colour=get_colour("ENDC")):
    """
    Print color text using escape codes
    """
    if sameline:
        sep = ''
    else:
        sep = '\n'
    sys.stdout.write(get_colour(colour) + text + bcolours["ENDC"] + sep)

printcolor = printcolour

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

def read_xy_pairs_from_csv(filename, X=0, y=1, sep=',', header=False):
    """Grab 2 columns from a csv file by name or col index
    
    Arguments:
        filename        Name of the csv file to read
        X               Index of the X column in the file [default: 0]
        y               Index of the y column in the file [default: 0]
        sep             Delimiter of the file [default: ,]
        header          Does the file have headers in row #1 [default: False]

    """
    with open(filename, 'r') as f:
        data = [line.strip() for line in f.readlines()]
        data = [line.split(sep) for line in data]
        data = [map(str.strip, row) for row in data]

    if isinstance(X, int) and isinstance(y, int):
        X_idx, y_idx = X, y
    elif isinstance(X, basestring) and isinstance(y, basestring) \
        and X.strip().isdigit() and y.strip().isdigit():
        X_idx = int(try_cast_str_to_number(X))
        y_idx = int(try_cast_str_to_number(y))
    else:
        X_idx, y_idx = None, None
    X_y_pairs = []
    for i, row in enumerate(data):
        if i == 0 and header:
            for j, col in enumerate(row):
                if col.strip().lower() == X.strip().lower():
                    X_idx = j
                if col.strip().lower() == y.strip().lower():
                    y_idx = j
            if (X_idx is None or y_idx is None):
                raise Exception("Column not found.")
        try:
            row = [try_cast_str_to_number(item) for item in row]
            if row[0] and row[1]:
                X_y_pairs.append(row)
        except Exception, err:
            pass
    return X_y_pairs



