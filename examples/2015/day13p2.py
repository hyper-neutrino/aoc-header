from aoc import *

a = set()
s = {}

for line in io.lines:
    x, _, y, *_, z = line[:-1].split()
    a |= {x, z}
    s.ensure(x, {})
    s[x][z] = (1 if y == "gain" else -1) * line.ints()[0]

a.add("_")
s["_"] = {}

for x in s:
    s["_"][x] = s[x]["_"] = 0

a.l.permutations().map(
    lambda x: x.sliding(wrap=True).mapsplat(lambda x, y: s[x][y] + s[y][x]).sum()
).max().print()
