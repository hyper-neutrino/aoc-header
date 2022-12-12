from aoc import *

g = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]

c = [0, 2].v

d = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}

for line in io.lines:
    for k in line:
        n = c + d[k]
        if 0 <= n[0] <= 4 >= n[1] >= 0 and g[n[1]][n[0]]:
            c = n
    print(g[c[1]][c[0]], end="")
