from aoc import *


def eval(regs, x):
    try:
        return int(x)
    except:
        return regs.get(x, 0)


lines = io.lines.map(str.split)

regs = ({"p": 0}, {"p": 1})
queues = ([], [])
i = [0, 0]

t = 0

while True:
    run = 0
    for p in [0, 1]:
        if 0 <= i[p] < lines.length:
            cmd, *x = lines[i[p]]
            if cmd == "snd":
                if p == 1:
                    t += 1
                queues[1 - p].append(eval(regs[p], x[0]))
            elif cmd == "set":
                regs[p][x[0]] = eval(regs[p], x[1])
            elif cmd == "add":
                regs[p][x[0]] = regs[p].get(x[0], 0) + eval(regs[p], x[1])
            elif cmd == "mul":
                regs[p][x[0]] = regs[p].get(x[0], 0) * eval(regs[p], x[1])
            elif cmd == "mod":
                regs[p][x[0]] = regs[p].get(x[0], 0) % eval(regs[p], x[1])
            elif cmd == "rcv":
                if queues[p].length == 0:
                    continue
                regs[p][x[0]] = queues[p].pop(0)
            elif cmd == "jgz":
                if eval(regs[p], x[0]) > 0:
                    i[p] += eval(regs[p], x[1])
                    run = 1
                    continue
            i[p] += 1
            run = 1
    if run == 0:
        break

print(t)
