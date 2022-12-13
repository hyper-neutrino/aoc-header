from aoc import *

io.lines.map(
    lambda x: x.ints()
    .permutations(2)
    .filter(lambda x: x[0] % x[1] == 0)[0]
    .reduce(floordiv_)
).sum().print()
