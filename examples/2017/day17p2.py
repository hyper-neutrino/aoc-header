from aoc import *

from collections import deque

x = io.ints[0]

o = 0
a = 0

for i in xrange(1, 50000001):
    if i % 1000000 == 0:
        print(i)
    a = (a + x) % i + 1
    if a == 1:
        o = i

print(o)

# NOTE: This solution runs a lot faster in PyPy. However, you will have to
# disable the header because forbiddenfruit is reliant on CPython