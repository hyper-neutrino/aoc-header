from aoc import *

d = io.data.ints() % 5

t = []

for x in intpart(100, len(d)):
    k = sum(x.v * d).l
    if k[-1] == 500:
        t.append(k[:-1].map(lambda x: max(x, 0)).reduce(mul_))

print(max(t))
