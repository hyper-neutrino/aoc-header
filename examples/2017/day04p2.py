from aoc import *

io.lines.map(str.split).vmap(lambda x: x.l.sort().t).countby(
    lambda x: x.s.length == x.length
).print()
