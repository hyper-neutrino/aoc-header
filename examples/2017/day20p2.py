from aoc import *

p = enumerate(io.ints % 9)

while True:
    for _, k in p:
        for i in range(3):
            k[3 + i] += k[6 + i]
            k[i] += k[3 + i]
    o = set()
    t = set()
    for k in p.map(lambda x: x[1][:3].t):
        if k in o:
            t.add(k)
        o.add(k)
    p = p.filter(lambda x: x[1][:3].t not in t)
    p.sort(key=lambda x: x[1][:3].map(abs).sum())
    if p.sortq(key=lambda x: x[1][-3:].map(abs).sum()):
        break

print(p.length)
