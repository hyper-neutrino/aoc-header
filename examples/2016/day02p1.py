from aoc import *

g = range(1, 10) % 3

c = [1, 1].v

d = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}

for line in io.lines:
    for k in line:
        n = c + d[k]
        if 0 <= n[0] <= 2 >= n[1] >= 0:
            c = n
    print(g[c[1]][c[0]], end="")
