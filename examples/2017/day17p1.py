from aoc import *

a = [0]

x = io.ints[0]

for i in range(2017):
    a <<= x + 1
    a.insert(0, i + 1)

a <<= a.index(2017)
print(a[1])
