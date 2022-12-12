from aoc import *

regs = {"a": 0, "b": 0, "c": 0, "d": 0}

eval = lambda x: (x.ints() or [regs[x]])[0]

lines = io.lines.map(str.split)

i = 0
while i < len(lines):
    cmd, *x = lines[i]
    if cmd == "cpy":
        regs[x[1]] = eval(x[0])
    elif cmd == "inc":
        regs[x[0]] += 1
    elif cmd == "dec":
        regs[x[0]] -= 1
    elif cmd == "jnz":
        if eval(x[0]):
            i += eval(x[1])
            continue
    i += 1

print(regs["a"])
