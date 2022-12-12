from aoc import *

from collections import deque

cache = {}

key = int(io.data)


def f(x, y):
    if x < 0 or y < 0:
        return 1
    if (x, y) not in cache:
        v = x * x + 3 * x + 2 * x * y + y + y * y + key
        t = 0
        while v:
            if v & 1:
                t ^= 1
            v >>= 1
        cache[(x, y)] = t
    return cache[(x, y)]


q = deque([(0, 1, 1)])
vis = {(1, 1)}

while q:
    d, x, y = q.popleft()
    for dx, dy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if (dx, dy) in vis:
            continue
        if f(dx, dy):
            continue
        vis.add((dx, dy))
        if d < 49:
            q.append((d + 1, dx, dy))

print(len(vis))
