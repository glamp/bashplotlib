

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
    r = start
    while r < stop:
        yield r
        r += step

