from aoc import *

i = 0
while True:
    for x, y in io.ints % 2:
        if (x + i) % ((y - 1) * 2) == 0:
            break
    else:
        print(i)
        break
    i += 1
