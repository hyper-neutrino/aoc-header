from aoc import *

v = int(io.data)

g = {0: 1}

d = 1
x = 0
r = 0

while True:
    if d in [1, -1]:
        r += 1
    for _ in range(r):
        x += d
        g[x] = sum(g.get(x + i + j * 1j, 0) for i, j in [-1, 0, 1] ** 2)
        if g[x] > v:
            print(g[x])
            exit(0)
    d *=- 1j