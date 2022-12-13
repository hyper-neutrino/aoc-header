from aoc import *

io.data.l.sliding(2, 1).filter(lambda x: x[0] == x[1]).map(
    lambda x: int(x[0])
).sum().print()
