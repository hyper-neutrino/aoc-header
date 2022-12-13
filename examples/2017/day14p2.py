from aoc import *


def knothash(s):
    a = range(256)
    pos = 0
    skip = 0

    items = s.l.map(ord) + [17, 31, 73, 47, 23]

    for _ in range(64):
        for i in items:
            a <<= pos
            a[:i] = a[:i][::-1]
            a >>= pos
            pos += i + skip
            skip += 1
            pos %= 256
            skip %= 256

    return (a % 16).map(lambda x: bin(x.reduce(xor_))[2:].zfill(8)).join()


grid = range(128).map(lambda x: knothash(io.data + "-" + x)).map(lambda x: map(int, x))

t = 0


def trav(r, c):
    for dr, dc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if len(grid) > dr >= 0 <= dc < len(grid[0]) and grid[dr][dc]:
            grid[dr][dc] = 0
            trav(dr, dc)


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c]:
            t += 1
            grid[r][c] = 0
            trav(r, c)

print(t)
