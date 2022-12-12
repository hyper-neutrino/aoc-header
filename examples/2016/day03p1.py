from aoc import *

io.lines.countby(lambda x: x.ints().sorted() * [1, 1, -1] > 0).print()
