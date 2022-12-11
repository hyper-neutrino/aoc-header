from aoc import *

a = io.data.ints()

t = sum(a) // 3

for i in range(len(a) + 1):
    for x in a.combinations(i):
        if sum(x) == t:
            print(product(x))
            exit(0)
