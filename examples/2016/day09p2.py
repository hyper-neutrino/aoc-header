from aoc import *


def s(x):
    t = 0
    while x:
        if x[0] != "(":
            t += 1
            x = x[1:]
            continue
        a, x = x[1:].split(")", 1)
        i, j = map(int, a.split("x"))
        t += s(x[:i]) * j
        x = x[i:]
    return t


print(s(io.data))
