from aoc import *

g = [".#.", "..#", "###"].map(list)

m = {}

for line in io.lines:
    l, r = line.split(" => ").map(lambda x: x.split("/").map(tuple).t)
    for _ in range(4):
        m[l] = r
        l = l[::-1]
        m[l] = r
        l = l.zip()

for _ in range(5):
    if len(g) % 2 == 0:
        i = 2
    else:
        i = 3
    c = len(g) // i
    n = c * (i + 1)
    n = [[0] * n for _ in range(n)]
    for ox in range(c):
        for oy in range(c):
            s = [[g[ox * i + x][oy * i + y] for y in range(i)].t for x in range(i)].t
            e = m[s]
            for x in range(i + 1):
                for y in range(i + 1):
                    n[ox * (i + 1) + x][oy * (i + 1) + y] = e[x][y]
    g = n

g.flat().count("#").print()
