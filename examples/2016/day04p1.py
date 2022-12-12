from aoc import *

t = 0

for line in io.lines:
    c = line[-6:-1]
    line = line[:-7]
    x = line.split("-")
    a = x[:-1].join("")
    i = int(x[-1])
    p = sorted(set(a), key=lambda x: (-a.count(x), x))
    if c.l == p[:5]:
        t += i

print(t)
