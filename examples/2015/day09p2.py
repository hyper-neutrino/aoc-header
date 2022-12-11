from aoc import *

a = set()
s = {}

for line in io.lines:
    x, _, y, _, z = line.split()
    a |= {x, y}
    s.ensure(x, {}).ensure(y, {})
    s[x][y] = s[y][x] = int(z)

a.permutations().map(
    lambda x: x.sliding().mapsplat(lambda x, y: s[x][y]).sum()
).max().print()
