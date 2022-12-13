from aoc import *

(io.data.l / 2).reduce(zip).filter(lambda x: x[0] == x[1]).map(
    lambda x: int(x[0]) * 2
).sum().print()
