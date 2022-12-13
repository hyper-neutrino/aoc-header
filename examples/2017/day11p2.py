from aoc import *

io.data.split(",").map(h2c.get).csum().map(
    lambda x: x.ri.map(abs).sum() // 2
).max().print()
