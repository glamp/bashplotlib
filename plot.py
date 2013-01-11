import string
import math
from collections import OrderedDict

def frange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def dist(x1, y1, x2, y2):
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)


class Plot(object):
    def __init__(self, size=21):
        self.size = size
        if self.size % 2 == 0:
            self.size += 1
        self.xaxis = list("-"*size)
        self.area = None

    def _setup_axis(self, xmin, xmax, ymin, ymax):
        self.y_axis = OrderedDict()
        self.x_axis = OrderedDict()
        for pos, y in enumerate(frange(ymin, ymax, (ymax-ymin)/float(self.size))):
            self.y_axis[y] = pos
        for pos, x in enumerate(frange(xmin, xmax, (xmax-xmin)/float(self.size))):
            self.x_axis[x] = self.size- 1 - pos

    def _create_area(self, xmin, xmax, ymin, ymax):
        self._setup_axis(xmin, xmax, ymin, ymax)
        self.area = []
        size = max([ymax - ymin, xmax - xmin])
        xmid = 0#(xmax - xmin)/float(self.size) + xmin
        ymid = 0#(self.size/2)*(ymax - ymin)/float(self.size) + ymin
        print xmid
        print ymid
        print xmin, xmax
        print ymin, ymax
        for y in frange(ymin, ymax, (ymax-ymin)/float(self.size)):
            row = []
            for x in frange(xmin, xmax, (xmax-xmin)/float(self.size)):
                #print x, y
                if y==ymid:
                    ch = "-"
                elif x==xmid:
                    ch = "|"
                else:
                    ch = " "
                row.append(ch)
            self.area.append(row)
        self.area.reverse() 

    def _add(self, x, y, pch="x"):
        xpos, ypos = None, None
        for i in self.x_axis:
            if i <= x:
                xpos = self.x_axis[i]
        for i in self.y_axis:
            if i <= y:
                ypos = self.y_axis[i]
        if xpos and ypos:
            self.area[ypos][xpos] = pch



    def _add_list(self, points):
        for point in points:
            self._add(point[0], point[1])

    def _render(self):
        for row in self.area:
            yield "".join(row)

    def plot(self, points, pch="x"):
        self.points = PointSet(points, pch)
        if self.area is None:
            self._create_area(self.points.x_min, self.points.x_max,
                              self.points.y_min, self.points.y_max)
        for p in self.points:
            self._add(p.x, p.y, pch)

    def show(self):
        for row in self._render():
            print row


class PointSet(object):
    def __init__(self, points, pch="x"):
        self.points = []
        self.x_min, self.x_max = 999999, -999999
        self.y_min, self.y_max = 999999, -999999
        
        for (x, y) in points: 
            self.points.append(Point(x, y, pch=pch))
            if x > self.x_max:
                self.x_max = x
            if x < self.x_min:
                self.x_min = x

            if y > self.y_max:
                self.y_max = y
            if y < self.y_min:
                self.y_min = y

    def __iter__(self):
        for point in self.points:
            yield point

class Point(object):
    def __init__(self, x, y, pch="x"):
        self.x = x
        self.y = y
        self.pch = pch



f1 = lambda x: x**2
f2 = lambda x: (2*x + 4)
f3 = lambda x: math.exp(x)
xs = range(-10, 10)

p = Plot(size=20)
points = [(x, f3(x)) for x in range(0, 10, 1)]
p.plot(points, "x")

p.show()


