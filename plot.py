import string
import math


def frange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step



class Plot(object):
    def __init__(self, size=21):
        self.xaxis = list("-"*size)


    def _create_area(self, xmin, xmax, ymin, ymax):
        self.area = []
        size = max([ymax - ymin, xmax - xmin])
        xmid = 10*(xmax - xmin)/20. + xmin
        ymid = 10*(ymax - ymin)/20. + ymin
        for y in frange(ymin, ymax, (ymax-ymin)/20.):
            row = []
            for x in frange(xmin, xmax, (xmax-xmin)/20.):
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
        if 
        self.area[y][x] = pch
    
    def _add_list(self, points):
        for point in points:
            self._add(point[0], point[1])

    def _render(self):
        for row in self.area:
            yield "".join(row)

    def plot(self, points):
        self.points = PointSet(points, "x")
        self._create_area(self.points.x_min, self.points.x_max,
                          self.points.y_min, self.points.y_max)
        for p in self.points.points:
            self._add(p.x, p.y, p.pch)
            print p.x, p.y

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



class Point(object):
    def __init__(self, x, y, pch="x"):
        self.x = x
        self.y = y
        self.pch = pch


p = Plot()

f1 = lambda x: x**2
f2 = lambda x: math.log(x)

xs = range(-10, 10)


points = [(x, f1(x)) for x in range(-10, 10)]
p.plot(points)



