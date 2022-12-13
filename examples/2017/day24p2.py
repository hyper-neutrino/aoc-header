from aoc import *

from collections import deque

ports = io.ints.t % 2

q = deque([(0, 0, 0, set(ports))])

m = 0
ml = 0

while q:
    d, l, n, s = q.popleft()
    if l > ml:
        ml = l
        m = d
    else:
        m = max(m, d)
    for x in s:
        if n in x:
            t = x[0] + x[1]
            q.append((d + t, l + 1, t - n, s - {x}))

print(m)
