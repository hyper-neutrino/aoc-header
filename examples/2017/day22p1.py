from aoc import *

s = set()

for r, row in enumerate(io.grid):
    for c, item in enumerate(row):
        if item == "#":
            s.add(r + c * 1j)

c = len(io.grid) // 2 * (1 + 1j)
d = -1

t = 0

for _ in range(10000):
    if c in s:
        d *= -1j
        s.remove(c)
    else:
        d *= 1j
        s.add(c)
        t += 1
    c += d

print(t)