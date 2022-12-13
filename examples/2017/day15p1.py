from aoc import *

A, B = io.ints

t = 0
m = (1 << 16) - 1

for _ in range(40000000):
    A = A * 16807 % 2147483647
    B = B * 48271 % 2147483647
    if (A ^ B) & m == 0:
        t += 1

print(t)
