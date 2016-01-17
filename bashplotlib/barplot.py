# -*- coding: utf-8 -*-

"""
Plotting terminal based barplots
"""

from .utils.helpers import *
from .histogram import calc_bins, read_numbers

def plot_bar(f, height=20.0, bincount=None, binwidth=None, pch="o",
    colour="default", title="", xlab=None, showSummary=False,
    regular=False, return_str=False):
    ''' Plot bar.

    Parameters
    ----------
    f : list(number), numpy.ndarray, str(filepath)
        input array
    height : float
        the height of the histogram in # of lines
    bincount : int
        number of bins in the histogram
    binwidth : int
        width of bins in the histogram
    pch : str
        shape of the bars in the plot, e.g 'o'
    colour : str
        white,aqua,pink,blue,yellow,green,red,grey,black,default,ENDC
    title : str
        title at the top of the plot, None = no title
    xlab : boolean
        whether or not to display x-axis labels
    showSummary : boolean
        whether or not to display a summary
    regular : boolean
        whether or not to start y-labels at 0
    return_str : boolean
        return string represent the plot or print it out, default: False

    Example
    -------
    >>> y = np.random.rand(50)
    >>> plot_bar(y, bincount=50, colour='red')

    >>> 0.971|
    >>> 0.923|                o         o             o   o
    >>> 0.875|                o   o     o           o o  oo
    >>> 0.827|                o   o     o     o     o o ooo
    >>> 0.779|   o            o   o     o   o o     o o ooo
    >>> 0.731|   o    o       o   o     o   o o     o o ooo
    >>> 0.683|   oo   oo      o   o o o o   o o     o o ooo
    >>> 0.635|   oo   oo      o  oo o o o   o o    oo o ooo
    >>> 0.587|   oo   oo      o  oo o ooo   o o    oo o ooo
    >>> 0.539|   oo   oo      o  oooo ooo   o o    oo o ooo o
    >>> 0.491|   ooo ooo      o  oooo ooo   o o   ooo o ooo o
    >>> 0.443|   ooo ooo     oo ooooo oooo  o o   ooo o ooo o
    >>> 0.395|   ooo ooo    ooooooooo oooo  o o   ooo o ooo o
    >>> 0.347|  oooo ooo    ooooooooo ooooo o o   ooo o ooo o
    >>> 0.299|  oooo ooo    ooooooooo ooooo o o   ooo o ooo o
    >>> 0.251|  oooo ooo    ooooooooo ooooo o o   ooo o ooo o o
    >>> 0.203|  oooo ooo    ooooooooo ooooo ooo   ooo o ooo o o
    >>> 0.155|  oooo ooo oo ooooooooo ooooo ooo   ooo ooooooo oo
    >>> 0.107| ooooo ooo oo ooooooooo oooooooooo  ooooooooooo ooo
    >>> 0.059| ooooo oooooo ooooooooo ooooooooooooooooooooooo ooo
    >>> 0.011| oooooooooooooooooooooo ooooooooooooooooooooooooooo
    >>>       --------------------------------------------------
    '''
    if pch is None:
        pch = "o"

    splot = ''
    if isinstance(f, str):
        f = open(f).readlines()

    # ====== Create data ====== #
    min_val, max_val = None, None
    n, mean, sd = 0.0, 0.0, 0.0

    # pick mode and get data
    numbers = [i for i in read_numbers(f)]
    int_mode = False
    if numbers[0].is_integer():
        int_mode = True

    # rescale big enough to show on bars
    min_orig = min(numbers) # original
    max_orig = max(numbers)
    numbers = [1000 * (i - min_orig) / (max_orig - min_orig + 1e-8) for i in numbers]

    # statistics
    n = len(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    mean = sum(numbers) / n
    sd = (sum([(mean - i)**2 for i in numbers]) / (n - 1)) ** 0.5

    # bins is index
    if bincount is not None:
        bincount = min(bincount, n)
    bins = list(calc_bins(n, 0., n + 0., bincount, binwidth))
    bins = [int(i) for i in bins]
    hist = dict((i, 0) for i in range(len(bins) - 1))

    # hist is the mean value of array with indices within bin
    for idx, (i, j) in enumerate(zip(bins, bins[1:])):
        arr = numbers[i:j]
        hist[idx] = sum(arr) / len(arr) # calculate mean

    # ====== Start plot ====== #
    min_y, max_y = min(hist.values()), max(hist.values())

    start = max(min_y, 1)
    stop = max_y + 1

    if regular:
        start = 1

    if height is None:
        height = stop - start
        if height > 20:
            height = 20

    ys = list(drange(start, stop, float(stop - start) / height))
    ys.reverse()

    nlen = max(len(str(min_y)), len(str(max_y))) + 1

    if title:
        splot += print_return_str(
            box_text(title, max(len(hist) * 2, len(title)), nlen),
            return_str=return_str)
    splot += print_return_str('', return_str=return_str)

    used_labs = set()
    for y in ys:
        if int_mode:
            ylab = '%d' % int(y * (max_orig - min_orig + 1e-8) / 1000 + min_orig)
        else:
            ylab = '%.3f' % float(y * (max_orig - min_orig + 1e-8) / 1000 + min_orig)
        if ylab in used_labs:
            ylab = ""
        else:
            used_labs.add(ylab)
        ylab = " " * (nlen - len(ylab)) + ylab + "|"

        splot += print_return_str(ylab, end=' ', return_str=return_str)

        for i in range(len(hist)):
            if int(y) <= hist[i]:
                splot += printcolour(pch, True, colour, return_str)
            else:
                splot += printcolour(" ", True, colour, return_str)
        splot += print_return_str('', return_str=return_str)
    xs = hist.keys()

    splot += print_return_str(" " * (nlen + 1) + "-" * len(xs),
                              return_str=return_str)

    if xlab:
        xlen = len(str(float((max_y) / height) + max_y))
        for i in range(0, xlen):
            splot += printcolour(" " * (nlen + 1), True, colour, return_str)
            for x in range(0, len(hist)):
                num = str(bins[x])
                if x % 2 != 0:
                    pass
                elif i < len(num):
                    splot += print_return_str(num[i], end=' ',
                                              return_str=return_str)
                else:
                    splot += print_return_str(" ", end=' ',
                                            return_str=return_str)
            splot += print_return_str('', return_str=return_str)

    center = max(map(len, map(str, [n, min_val, mean, max_val])))
    center += 15

    if showSummary:
        splot += print_return_str('', return_str=return_str)
        splot += print_return_str("-" * (2 + center), return_str=return_str)
        splot += print_return_str("|" + "Summary".center(center) + "|",
                                  return_str=return_str)
        splot += print_return_str("-" * (2 + center), return_str=return_str)
        summary = "|" + ("observations: %d" % n).center(center) + "|\n"
        summary += "|" + ("min value: %f" % min_val).center(center) + "|\n"
        summary += "|" + ("mean : %f" % mean).center(center) + "|\n"
        summary += "|" + ("sd : %f" % sd).center(center) + "|\n"
        summary += "|" + ("max value: %f" % max_val).center(center) + "|\n"
        summary += "-" * (2 + center)
        splot += print_return_str(summary, return_str=return_str)

    if return_str:
        return splot
