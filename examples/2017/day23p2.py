from aoc import *

h = 0
b = io.ints[0] * 100 + 100000

for x in range(b, b + 17001, 17):
    for i in range(2, x**0.5 + 1):
        if x % i == 0:
            h += 1
            break

print(h)
