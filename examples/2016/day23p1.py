from aoc import *

regs = {"a": 7, "b": 0, "c": 0, "d": 0}

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
    elif cmd == "tgl":
        try:
            line = lines[i + eval(x[0])]
            line[0] = {
                "inc": "dec",
                "dec": "inc",
                "tgl": "inc",
                "jnz": "cpy",
                "cpy": "jnz",
            }[line[0]]
        except:
            pass
    i += 1

print(regs["a"])
