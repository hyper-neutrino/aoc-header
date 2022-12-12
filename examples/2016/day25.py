from aoc import *

a = 1

lines = (
    io.data.replace(
        """cpy a d
cpy 4 c
cpy 643 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a""",
        """add 2572 a
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0""",
    )
    .lines()
    .map(str.split)
)

while True:
    regs = {"a": a, "b": 0, "c": 0, "d": 0}

    eval = lambda x: (x.ints() or [regs[x]])[0]

    output = []

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
        elif cmd == "add":
            regs[x[1]] += eval(x[0])
        elif cmd == "out":
            output.append(eval(x[0]))
            if output != [output[0], 1 - output[0]] * (len(output) / 2):
                break
            if len(output) >= 10:
                print(a)
                exit(0)
        i += 1

    a += 1
