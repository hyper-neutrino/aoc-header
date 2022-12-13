from aoc import *

from collections import deque

adj = {}

for line in io.lines:
    l, r = line.split(" <-> ")
    l = int(l)
    r = map(int, r.split(", "))
    adj.ensure(l, set())
    for k in r:
        adj.ensure(k, set())
        adj[l].add(k)
        adj[k].add(l)

q = deque([0])
t = {0}

while q:
    n = q.popleft()
    for k in adj[n]:
        if k in t:
            continue
        t.add(k)
        q.append(k)

print(len(t))
