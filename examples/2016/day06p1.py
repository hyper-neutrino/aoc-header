from aoc import *

io.grid.zip().map(lambda x: x.maximal(x.count)[0]).join("").print()
