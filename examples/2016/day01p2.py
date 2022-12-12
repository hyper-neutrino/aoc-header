from aoc import *

s = {0}
t = 0
d = 1

for x in io.data.split(", "):
    if x[0] == "R":
        d *= 1j
    else:
        d /= 1j
    for _ in range(int(x[1:])):
        t += d
        if t in s:
            t.ir.map(abs).sum().print()
            exit(0)
        s.add(t)
