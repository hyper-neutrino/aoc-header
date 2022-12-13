from aoc import *

io.lines.map(lambda x: x.ints()).map(lambda x: max(x) - min(x)).sum().print()
