from aoc import *

(io.data.ints() % 4).mapsplat(lambda i, m, _, x: (m, (-x - i) % m)).zip().callsplat(
    crt
).print()
