from aoc import *

v = int(io.data)

r = 0
x = 1
d = 0
m = 0

while True:
    if x + d + (2 if m == 0 else 0) > v:
        break
    if m == 0:
        r += 1
        d += 2
        m = 4
    m -= 1
    x += d

print(r + abs(v - x - d // 2))
