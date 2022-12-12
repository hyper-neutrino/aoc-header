from aoc import *

valid = [(0, 4294967295)]

for x, y in io.data.replace("-", " ").ints() % 2:
    o = []
    for s, e in valid:
        if y < s or x > e:
            o.append((s, e))
        elif x <= s and y >= e:
            pass
        elif x <= s:
            o.append((y + 1, e))
        elif y >= e:
            o.append((s, x - 1))
        else:
            o.append((s, x - 1))
            o.append((y + 1, e))
    valid = o

valid.mapsplat(lambda x, y: y - x + 1).sum().print()
