from aoc import *

d = io.data.ints() % 5

t = []

for x in intpart(100, len(d)):
    t.append(sum(x.v * d).l[:-1].map(lambda x: max(x, 0)).reduce(mul_))

print(max(t))
