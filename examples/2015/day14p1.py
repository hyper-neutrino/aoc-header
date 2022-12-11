from aoc import *

a = io.data.ints() % 3
b = [[1, x[1], 0] for x in a]


for _ in range(2503):
    for [x, y, z], k in zip(a, b):
        if k[0]:
            k[2] += x
        k[1] -= 1
        if k[1] == 0:
            k[0] ^= 1
            k[1] = y if k[0] else z

b.map(lambda x: x[2]).max().print()
