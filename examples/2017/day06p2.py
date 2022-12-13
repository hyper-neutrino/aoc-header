from aoc import *

b = io.ints

s = {b.t: 0}

i = 0

while True:
    i += 1
    k = b.index(max(b))
    t = b[k]
    b[k] = 0
    q, r = divmod(t, len(b))
    for p in range(k + 1, k + r + 1):
        b[p % len(b)] += q + 1
    for p in range(k + r + 1, k + len(b) + 1):
        b[p % len(b)] += q
    if b.t in s:
        print(i - s[b.t])
        break
    s[b.t] = i
