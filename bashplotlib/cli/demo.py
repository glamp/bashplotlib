#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""demo.py
"""
import os, sys
from bashplotlib.cli.hist import __doc__ as HIST_DOCSTRING
from bashplotlib.core.histogram import plot_hist
from bashplotlib import PROJECT_ROOT

DATA_PATH = os.path.realpath(os.path.join(PROJECT_ROOT, '..', 'data'))

if not os.path.exists(DATA_PATH):
    sys.stderr.write('You need to download the example data set to run the demo...')
    sys.stderr.write('try running `./examples/downloaddata.sh` to get the data')
    sys.exit(1)

def _hist_demo():
    f = os.path.join(DATA_PATH, 'exp.txt')
    print f
    plot_hist(f)

def run_demo(command):
    if command == "hist":
        _hist_demo()
    elif command == "scatter":
        raise NotImplementedError('`run_demo` is only implemented for `hist` cmd so far.')
