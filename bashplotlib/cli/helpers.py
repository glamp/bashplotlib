#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""cli/helpers.py
"""
import sys, os
from select import select

def read_stdin_or_timeout():
    """Try reading stdin. give up in 0.5s if nothing read yet."""
    timeout = 0.5
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        return sys.stdin.readlines()
    else:
        return None

