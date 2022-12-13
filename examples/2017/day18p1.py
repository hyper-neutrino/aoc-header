from aoc import *

regs = {}

def eval(x):
    try:
        return int(x)
    except:
        return regs.get(x, 0)

lines = io.lines.map(str.split)

i = 0
s = None
while 0 <= i < lines.length:
    cmd, *x = lines[i]
    if cmd == "snd":
        s = eval(x[0])
    elif cmd == "set":
        regs[x[0]] = eval(x[1])
    elif cmd == "add":
        regs[x[0]] = regs.get(x[0], 0) + eval(x[1])
    elif cmd == "mul":
        regs[x[0]] = regs.get(x[0], 0) * eval(x[1])
    elif cmd == "mod":
        regs[x[0]] = regs.get(x[0], 0) % eval(x[1])
    elif cmd == "rcv":
        if eval(x[0]) != 0:
            print(s)
            break
    elif cmd == "jgz":
        if eval(x[0]) > 0:
            i += eval(x[1])
            continue
    i += 1