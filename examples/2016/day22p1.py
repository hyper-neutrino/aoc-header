from aoc import *

(io.data.ints() % 6).permutations(2).mapsplat(
    lambda x, y: x[3] and x[3] <= y[4]
).countby().print()
