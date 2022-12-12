from aoc import *

screen = [[0] * 50 for _ in range(6)]

for line in io.lines:
    if line.startswith("re"):
        x, y = line.ints()
        for c in range(x):
            for r in range(y):
                screen[r][c] = 1
    elif line.startswith("rotate r"):
        r, v = line.ints()
        screen[r] >>= v
    else:
        c, v = line.ints()
        screen = screen.zip()
        screen[c] >>= v
        screen = screen.zip()

screen.flat().sum().print()
