from aoc import *

x = int(io.data)

i = 1

while True:
    f = {k for q in range(1, int(i**0.5)) if i % q == 0 for k in [q, i // q]}
    if sum(f) * 10 >= x:
        break
    i += 1

print(i)
