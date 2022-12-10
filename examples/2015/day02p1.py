from aoc import *

io.data.ints().chunks(3).map(sorted).mapsplat(
    lambda x, y, z: 2 * (x * y + y * z + z * x) + x * y
).sum().print()
