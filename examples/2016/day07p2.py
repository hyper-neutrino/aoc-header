from aoc import *

import re

t = 0

for line in io.lines:
    mode = 1
    a = set()
    b = set()
    for x in line.l.sliding(3):
        if x[0] == "[":
            mode = 0
        elif x[0] == "]":
            mode = 1
        if x[0] == x[2] != x[1]:
            if mode:
                a.add((x[0], x[1]))
            else:
                b.add((x[1], x[0]))
    else:
        t += bool(a & b)

print(t)