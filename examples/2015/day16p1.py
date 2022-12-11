from aoc import *

k = {}

for line in """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".lines():
    x, y = line.split(": ")
    k[x] = int(y)


for line in io.lines:
    n = line.ints()[0]
    for p in line.split(": ", 1)[1].split(", "):
        x, y = p.split(": ")
        if k[x] != int(y):
            break
    else:
        print(n)
