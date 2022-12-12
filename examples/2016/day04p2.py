from aoc import *

t = 0

for line in io.lines:
    c = line[-6:-1]
    line = line[:-7]
    x = line.split("-")
    a = x[:-1].join("")
    i = int(x[-1])
    k = a.ord().map(lambda x: (x - 97 + i) % 26 + 97).chr()
    if "northpole" in k:
        print(i)