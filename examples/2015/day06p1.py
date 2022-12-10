from aoc import *

grid = [[0] * 1000 for _ in range(1000)]

for x in io.lines:
    mode = x[:7]
    x1, y1, x2, y2 = x.ints()
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if mode == "turn on":
                grid[x][y] = 1
            elif mode == "turn of":
                grid[x][y] = 0
            else:
                grid[x][y] ^= 1

print(sum(map(sum, grid)))
