from aoc import *

s = "abcdefgh".l

for line in io.lines:
    x = line.split()
    cmd = x[0]

    if cmd == "swap":
        a, b = map(int if x[1] == "position" else s.index, x[2::3])
        s[a], s[b] = s[b], s[a]
    elif cmd == "rotate":
        if x[1] == "left":
            s <<= int(x[2])
        elif x[1] == "right":
            s >>= int(x[2])
        else:
            i = s.index(x[6])
            s >>= 1 + i + (i >= 4)
    elif cmd == "reverse":
        a, b = map(int, x[2::2])
        s[a : b + 1] = s[a : b + 1][::-1]
    elif cmd == "move":
        a, b = map(int, x[2::3])
        s.insert(b, s.pop(a))

print(s.join())
