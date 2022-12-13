from aoc import *

x = set()
e = set()

for line in io.lines:
    if "->" in line:
        line, r = line.split(" -> ")
        e |= set(r.split(", "))
    x.add(line.split()[0])

(k,) = x - e
print(k)
