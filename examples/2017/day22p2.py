from aoc import *

g = {}

for r, row in enumerate(io.grid):
    for c, item in enumerate(row):
        g[r + c * 1j] = (item == "#") * 2

c = len(io.grid) // 2 * (1 + 1j)
d = -1

t = 0

for _ in range(10000000):
    n = g.get(c, 0)
    d *= 1j * (-1j) ** n
    g[c] = (n + 1) % 4
    if n == 1:
        t += 1
    c += d

print(t)
