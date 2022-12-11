from aoc import *

x = io.data

for _ in range(50):
    x = rle(x, 1, 1).join("")

print(len(x))
