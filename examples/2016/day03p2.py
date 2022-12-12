from aoc import *

(io.data.ints() % 3 % 3).mapsplat(zip).nflat().countby(
    lambda x: x.sorted() * [1, 1, -1] > 0
).print()
