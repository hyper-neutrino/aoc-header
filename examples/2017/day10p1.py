from aoc import *

a = range(256)

pos = 0
skip = 0

for i in io.ints:
    a <<= pos
    a[:i] = a[:i][::-1]
    a >>= pos
    pos += i + skip
    skip += 1

print(a[0] * a[1])
