from aoc import *

regs = {"a": 12, "b": 0, "c": 0, "d": 0}

eval = lambda x: (x.ints() or [regs[x]])[0]

lines = (
    io.data.replace(
        """cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
""",
        """mul b d a
cpy 0 c
cpy 0 d
jnz 0 0
jnz 0 0
jnz 0 0
""",
    )
    .lines()
    .map(str.split)
)

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
    elif cmd == "mul":
        regs[x[2]] = eval(x[0]) * eval(x[1])
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
