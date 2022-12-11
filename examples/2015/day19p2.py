from aoc import *

*x, _, m = io.lines

t = 0

for line in x:
    a, b = line.split(" => ")
    if b in m:
        t += 1
        m = m.replace(b, a, 1)
    if m == "e":
        break
    x.append(line)

print(t)
