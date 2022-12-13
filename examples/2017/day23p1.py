from aoc import *

regs = {x: 0 for x in "abcdefgh"}


def eval(x):
    return regs[x] if x in regs else int(x)


lines = io.lines.map(str.split)

i = 0
t = 0

while 0 <= i < lines.length:
    cmd, x, y = lines[i]

    if cmd == "set":
        regs[x] = eval(y)
    elif cmd == "sub":
        regs[x] -= eval(y)
    elif cmd == "mul":
        regs[x] *= eval(y)
        t += 1
    elif cmd == "jnz":
        if eval(x) != 0:
            i += eval(y)
            continue
    i += 1

print(t)
