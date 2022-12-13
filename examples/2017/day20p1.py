from aoc import *

enumerate(io.ints % 9).minimal(lambda x: x[1][-3:].map(abs).sum()).minimal(
    lambda x: (x[1][-6:-3].v * sign(x[1][-3:]).map(abs).sum())
).minimal(lambda x: (x[1][:3].v * sign(x[1][-6:-3]).map(abs).sum()))[0][0].print()
