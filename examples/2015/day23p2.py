from aoc import *

registers = {"a": 1, "b": 0}

lines = io.lines.map(lambda x: x.replace(",", "").split())

i = 0
while i < len(lines):
    line = lines[i]
    cmd = line[0]

    if cmd == "hlf":
        registers[line[1]] //= 2
        i += 1
    elif cmd == "tpl":
        registers[line[1]] *= 3
        i += 1
    elif cmd == "inc":
        registers[line[1]] += 1
        i += 1
    elif cmd == "jmp":
        i += int(line[1])
    elif cmd == "jie":
        if registers[line[1]] % 2 == 0:
            i += int(line[2])
        else:
            i += 1
    elif cmd == "jio":
        if registers[line[1]] == 1:
            i += int(line[2])
        else:
            i += 1

print(registers["b"])
