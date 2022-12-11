from aoc import *

*x, _, m = io.lines

s = set()

for line in x:
    a, b = line.split(" => ")
    i = 0
    while True:
        i = m.find(a, i)
        if i == -1:
            break
        s.add(m[:i] + b + m[i + len(a) :])
        i += 1

print(len(s))
