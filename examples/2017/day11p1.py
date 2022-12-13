from aoc import *

print(io.data.split(",").map(h2c.get).sum().ri.map(abs).sum() // 2)
