from aoc import *

t = 0
d = 0

g = 0
s = 0

for c in io.data:
    if s:
        s = 0
        continue
    if g:
        if c == ">":
            t += d
            d = 0
            g = 0
        elif c == "!":
            s = 1
        else:
            d += 1
    else:
        if c == "<":
            g = 1

print(t)
