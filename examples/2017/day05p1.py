from aoc import *

d = io.ints

i = 0
s = 0

while 0 <= i < len(d):
    s += 1
    d[i] += 1
    i += d[i] - 1

print(s)