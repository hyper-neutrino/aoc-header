from aoc import *

from collections import deque

nodes = io.data.ints() % 6

((x, y, S, _, _, _),) = nodes.filterout(lambda x: x[3])

q = deque([(0, x, y, [])])

mx, my, *_ = nodes[-1]

l = -1
grid = []
for x, y, _, u, _, _ in nodes:
    if l != x:
        l = x
        grid.append([])
    grid[-1].append(u)

vis = grid.vmap(lambda _: 0)

p = 0

while q:
    d, x, y, a = q.popleft()
    for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if mx >= dx >= 0 <= dy <= my and grid[dx][dy] <= S and not vis[dx][dy]:
            if dx == mx - 1 and dy == 0:
                p = d + 1
                break
            vis[dx][dy] = 1
            q.append((d + 1, dx, dy, a + [(dx, dy)]))
    else:
        continue
    break

print(p + 5 * (mx - 1) + 1)
