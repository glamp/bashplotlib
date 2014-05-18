#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage messages for bashplotlib system commands
"""

hist = {
    "usage": """hist is a command for making histograms. it accepts a series of values in one of the following formats:
        1) txt file w/ 1 column of numbers
        2) standard in piped from another command line cat or curl

    for some examples of how to use hist, you can type the command:
        hist --demo
    or visit https://github.com/glamp/bashplotlib/blob/master/examples/sample.sh
    """
}

scatter = {
    "usage": """scatterplot is a command for making xy plots. it accepts a series of x values and a series of y values in the
    following formats:
        1) a txt file or standard in value w/ 2 comma seperated columns of x,y values
        2) 2 txt files. 1 w/ designated x values and another with designated y values.

    scatter -x <xcoords> -y <ycoords>
    cat <file_with_x_and_y_coords> | scatter
    """
}
