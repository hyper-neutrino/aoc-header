from aoc import *

p = lower[:16].l

i = 0


def f():
    global p

    for ins in io.data.split(","):
        if ins[0] == "s":
            p >>= int(ins[1:])
        elif ins[0] == "x":
            x, y = map(int, ins[1:].split("/"))
            p.swap(x, y)
        elif ins[0] == "p":
            x, y = map(p.index, ins[1::2])
            p.swap(x, y)


while True:
    i += 1
    f()
    if p == lower[:16].l:
        break

for _ in range(1000000000 % i):
    f()

p.join().print()
