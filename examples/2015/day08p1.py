from aoc import *

io.lines.map(lambda x: len(x) - len(eval(x))).sum().print()
