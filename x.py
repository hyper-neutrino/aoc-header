from aoc import *

t = 0
I = 0

def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return 1 if x < y else -1 if x > y else 0
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])
        for i in range(max(len(x), len(y))):
            if i >= len(x):
                return 1
            if i >= len(y):
                return -1
            v = f(x[i], y[i])
            if v:
                return v
        return 0

for x, y in io.data.split("\n\n").map(str.splitlines):
    I += 1
    x = eval(x)
    y = eval(y)
    if f(x, y) == 1:
        t += I

print(t)