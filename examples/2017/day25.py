from aoc import *

tape = set()

g = io.blocks

x, y = g.pop(0).splitlines()
state = x.split()[-1][:-1]
steps = y.ints()[0]

trans = {}

for b in g:
    x, _, n1, d1, s1, _, n2, d2, s2 = b.strip().splitlines()
    trans[x.split()[-1][:-1]] = ((n1, d1, s1), (n2, d2, s2)).mapsplat(
        lambda n, d, s: (int(n[-2]), 1 if "right" in d else -1, s.split()[-1][:-1])
    )

pos = 0

for _ in range(steps):
    n, d, s = trans[state][pos in tape]

    if n:
        tape.add(pos)
    else:
        tape.discard(pos)

    pos += d
    state = s

print(len(tape))
