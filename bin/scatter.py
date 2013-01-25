import csv

def drange(start, stop, step=1.0):
    "generate between 2 numbers w/ optional step"
    r = start
    while r < stop:
        yield r
        r += step

def get_scale(series, is_y=False, steps=20):
    min_val = min(series)
    max_val = max(series)
    scaled_series = []
    for x in drange(min_val, max_val, (max_val-min_val)/steps):
        if x > 0 and scaled_series and max(scaled_series) < 0:
            scaled_series.append(0.0)
        scaled_series.append(x)
    
    if is_y:
        scaled_series.reverse()
    return scaled_series


f = "test.txt"
f = "bigtest.txt"
f = "coords.txt"
f = "texas.txt"

if f:
    data = [tuple(map(float, line)) for line in csv.reader(open(f))]
else:
    xs = xs
    ys = ys
xs = [i[0] for i in data]
ys = [i[1] for i in data]

size = 20

plotted = set()

print "-"*(2*len(get_scale(xs, False, size))+2)
for y in get_scale(ys, True, size):
    print "|",
    for x in get_scale(xs, False, size):
        point = " "
        for (i, (xp, yp)) in enumerate(zip(xs, ys)):
            if xp <= x and yp >= y and (xp, yp) not in plotted:
                point = "x"
                #point = str(i) 
                plotted.add((xp, yp))
        if x==0 and y==0:
            point = "o"
        elif x==0:
            point = "|"
        elif y==0:
            point = "-"
        print point,
    print "|"
print "-"*(2*len(get_scale(xs, False, size))+2)
                    



