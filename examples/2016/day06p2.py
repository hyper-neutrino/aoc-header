from aoc import *

io.grid.zip().map(lambda x: x.minimal(x.count)[0]).join("").print()
