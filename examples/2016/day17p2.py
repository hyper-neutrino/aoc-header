from aoc import *

from collections import deque

q = deque([(0, "", 0, 0)])

m = 0

while q:
    d, s, x, y = q.popleft()
    if x == y == 3:
        m = d
        continue
    U, D, L, R = md5(io.data + s)[:4].l.map(lt_ & "a")
    if x > 0 and U:
        q.append((d + 1, s + "U", x - 1, y))
    if x < 3 and D:
        q.append((d + 1, s + "D", x + 1, y))
    if y > 0 and L:
        q.append((d + 1, s + "L", x, y - 1))
    if y < 3 and R:
        q.append((d + 1, s + "R", x, y + 1))

print(m)
