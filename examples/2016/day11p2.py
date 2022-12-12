from aoc import *

import re
from collections import deque

floors = []

for line in io.lines:
    gens = tuple(re.findall(r"(\w+) generator", line))
    chips = tuple(re.findall(r"(\w+)-compatible microchip", line))
    floors.append((gens, chips))

floors[0] = floors[0].map(lambda x: x + ("elerium", "dilithium"))

q = deque([(0, 0, tuple(floors))])
vis = set()

while q:
    m, f, x = q.popleft()
    if x[:-1].all(lambda r: r[0].length + r[1].length == 0):
        print(m)
        break
    k = []
    for i in [0, 1]:
        for n in x[f][i]:
            k.append((i, n))
    k = tuple(k)

    j1 = []
    j2 = []

    for t in k:
        for t2 in k + (None,):
            if t == t2:
                continue
            if t2 is None:
                j1.append((t,))
            else:
                j2.append((t, t2))

    for n in [f - 1, f + 1]:
        p1 = j1 if n < f else j2
        p2 = j2 if n < f else j1

        for p in [p1, p2]:
            V = 0
            for t in p:
                if 0 <= n < x.length:
                    if n < f and range(f).all(
                        lambda i: x[i][0].length + x[i][1].length == 0
                    ):
                        continue
                    g = list(x)
                    for i, v in t:
                        g[f] = list(g[f])
                        g[f][i] = g[f][i] - v
                        g[f] = tuple(g[f])

                        g[n] = list(g[n])
                        g[n][i] = g[n][i] + (v,)
                        g[n] = tuple(g[n])
                    g = tuple(g)
                    T = {}
                    I = 1

                    def tt(x):
                        global I
                        if x not in T:
                            T[x] = I
                            I *= 2
                        return T[x]

                    key = g.map(lambda x: x.map(lambda y: y.map(tt).sum()))

                    if (n, key) in vis:
                        continue

                    vis.add((n, key))

                    for r in g:
                        if r[0] and not r[1].all(in_ & (None, r[0])):
                            break
                    else:
                        V = 1
                        q.append((m + 1, n, g))
            if V:
                break
