from aoc import *

from collections import deque

adj = {x: {} for x in io.ints}

grid = io.grid.vmap(eq_ & "#")

pos = {}

for r, row in enumerate(io.grid):
    for c, item in enumerate(row):
        if item.isdigit():
            pos[int(item)] = (r, c)


def bfs(sx, sy, ex, ey):
    q = deque([(0, sx, sy)])
    vis = {(sx, sy)}
    while q:
        d, x, y = q.popleft()
        for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if grid[dx][dy] or (dx, dy) in vis:
                continue
            if dx == ex and dy == ey:
                return d + 1
            vis.add((dx, dy))
            q.append((d + 1, dx, dy))


for i, j in list(pos).combinations(2):
    adj[i][j] = adj[j][i] = bfs(*pos[i], *pos[j])

(list(pos) - 0).permutations().map(
    lambda x: x.prepend(0).sliding(2, 1).mapsplat(lambda x, y: adj[x][y]).sum()
).min().print()
