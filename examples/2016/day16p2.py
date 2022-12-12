from aoc import *

data = map(int, io.data)

s = 35651584

while len(data) < s:
    data.append(0)
    for i in range(len(data) - 2, -1, -1):
        data.append(1 - data[i])

data = data[:s]

while len(data) % 2 == 0:
    data = [data[i] == data[i + 1] for i in range(0, len(data), 2)]

print(data.map(int).join(""))
