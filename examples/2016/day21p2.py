from aoc import *

s = "fbgdceah".l

for line in io.lines[::-1]:
    x = line.split()
    cmd = x[0]

    if cmd == "swap":
        a, b = map(int if x[1] == "position" else s.index, x[2::3])
        s[a], s[b] = s[b], s[a]
    elif cmd == "rotate":
        if x[1] == "left":
            s >>= int(x[2])
        elif x[1] == "right":
            s <<= int(x[2])
        else:
            o = s[:]
            while True:
                i = o.index(x[6])
                if o >> 1 + i + (i >= 4) == s:
                    break
                o <<= 1
            s = o
    elif cmd == "reverse":
        a, b = map(int, x[2::2])
        s[a : b + 1] = s[a : b + 1][::-1]
    elif cmd == "move":
        a, b = map(int, x[2::3])
        s.insert(a, s.pop(b))

print(s.join())
