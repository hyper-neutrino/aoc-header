from aoc import *

import heapq

bhp, batk = io.data.ints()

pq = []
heapq.heappush(pq, (0, bhp, batk, 50, 500, 0, 0, 0))

while pq:
    s, bh, ba, ph, m, S, P, R = heapq.heappop(pq)
    
    ph -= 1
    if ph <= 0:
        continue

    if S:
        S -= 1
    if P:
        bh -= 3
        P -= 1
    if R:
        m += 101
        R -= 1

    if bh <= 0:
        print(s)
        exit(0)

    o = []

    if m >= 53:
        o.append((s + 53, bh - 4, ba, ph, m - 53, S, P, R))

    if m >= 73:
        o.append((s + 73, bh - 2, ba, ph + 2, m - 73, S, P, R))

    if m >= 113 and not S:
        o.append((s + 113, bh, ba, ph, m - 113, 6, P, R))

    if m >= 173 and not P:
        o.append((s + 173, bh, ba, ph, m - 173, S, 6, R))

    if m >= 229 and not R:
        o.append((s + 229, bh, ba, ph, m - 229, S, P, 5))

    for s, bh, ba, ph, m, S, P, R in o:
        a = 0

        if S:
            a = 7
            S -= 1
        if P:
            bh -= 3
            P -= 1
        if R:
            m += 101
            R -= 1

        if bh <= 0:
            print(s)
            exit(0)

        ph -= max(ba - a, 1)

        if ph > 0:
            heapq.heappush(pq, (s, bh, ba, ph, m, S, P, R))
