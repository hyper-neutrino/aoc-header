from aoc import *
import time

x = io.data

for _ in range(40):
    x = rle(x, 1, 1).join("")

print(len(x))
