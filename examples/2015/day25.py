from aoc import *

r, c = io.data.ints()

x = r + c - 1
i = x * (x - 1) // 2 + c

print(20151125 * pow(252533, i - 1, 33554393) % 33554393)
