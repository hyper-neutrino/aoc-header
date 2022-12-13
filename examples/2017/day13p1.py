from aoc import *

(io.ints % 2).filter(lambda x: x[0] % ((x[1] - 1) * 2) == 0).mapsplat(
    mul_
).sum().print()
