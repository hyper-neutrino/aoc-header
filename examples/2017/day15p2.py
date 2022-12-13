from aoc import *

A, B = io.ints

t = 0
m = (1 << 16) - 1

for _ in range(5000000):
    while True:
        A = A * 16807 % 2147483647
        if A % 4 == 0:
            break
    while True:
        B = B * 48271 % 2147483647
        if B % 8 == 0:
            break
    if (A ^ B) & m == 0:
        t += 1

print(t)
