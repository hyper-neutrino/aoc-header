from aoc import *

row = io.data.tl(".", 0).tl("^", 1)

t = 0
for _ in range(40):
    t += row.count(0)
    row = [
        int(
            4 * (0 if i == 0 else row[i - 1])
            + 2 * row[i]
            + (0 if i == len(row) - 1 else row[i + 1])
            in [6, 4, 3, 1]
        )
        for i in range(len(row))
    ]

print(t)
