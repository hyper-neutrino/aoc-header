from aoc import *

grid = io.grid.vtl({"#": 1, ".": 0})


def f():
    grid[0][0] = grid[0][-1] = grid[-1][0] = grid[-1][-1] = 1


f()

for _ in range(100):
    new = grid.vmap(id)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new[r][c] = sum(
                grid[dr][dc] if len(grid) > dr >= 0 <= dc < len(grid[0]) else 0
                for dr in range(r - 1, r + 2)
                for dc in range(c - 1, c + 2)
            ) in ([3, 4] if grid[r][c] else [3])
    grid = new
    f()

grid.map(sum).sum().print()
