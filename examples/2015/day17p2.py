from aoc import *

io.data.ints().powerset().filter(lambda x: sum(x) == 150).minimal(len).length.print()
