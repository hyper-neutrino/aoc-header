from aoc import *

t = 0
d = 1

for x in io.data.split(", "):
    if x[0] == "R":
        d *= 1j
    else:
        d /= 1j
    t += int(x[1:]) * d

t.ir.map(abs).sum().print()
