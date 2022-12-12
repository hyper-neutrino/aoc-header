from aoc import *

import re

t = 0

for line in io.lines:
    mode = 1
    valid = 0
    for x in line.l.sliding(4):
        if x[0] == "[":
            mode = 0
        elif x[0] == "]":
            mode = 1
        if x[0] == x[3] and x[1] == x[2] and x[0] != x[1]:
            if mode:
                valid = 1
            else:
                break
    else:
        t += valid

print(t)