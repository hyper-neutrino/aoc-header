from aoc import *


def knothash(s):
    a = range(256)
    pos = 0
    skip = 0

    items = s.l.map(ord) + [17, 31, 73, 47, 23]

    for _ in range(64):
        for i in items:
            a <<= pos
            a[:i] = a[:i][::-1]
            a >>= pos
            pos += i + skip
            skip += 1
            pos %= 256
            skip %= 256

    return (a % 16).map(lambda x: bin(x.reduce(xor_))[2:].zfill(8)).join()


range(128).map(lambda x: knothash(io.data + "-" + x)).join().count("1").print()
