from aoc import *

from collections import deque

L, R = map(deque, range(1, 1 + int(io.data)) / 2)

while L and R:
    if len(L) > len(R):
        L.pop()
    else:
        R.popleft()

    R.append(L.popleft())
    L.append(R.popleft())

print(L[0] or R[0])
