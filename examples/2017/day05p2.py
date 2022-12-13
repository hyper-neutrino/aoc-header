from aoc import *

d = io.ints

i = 0
s = 0

while 0 <= i < len(d):
    s += 1
    n = i + d[i]
    if d[i] >= 3:
        d[i] -= 1
    else:
        d[i] += 1
    i = n

print(s)