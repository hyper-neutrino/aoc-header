from aoc import *

hashes = {}
cache = {}


def h(i):
    if i not in hashes:
        hashes[i] = md5(io.data + i)
        for _ in range(2016):
            hashes[i] = md5(hashes[i])
    return hashes[i]


i = -1
q = 64

while q:
    i += 1
    x = h(i).l.sliding(3).filter(lambda x: x.s.length == 1)
    if x:
        if range(i + 1, i + 1001).any(lambda g: [x[0][0]] * 5 in h(g).l.sliding(5)):
            q -= 1

print(i)
