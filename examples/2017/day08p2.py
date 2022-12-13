from aoc import *

regs = {}

m = -float("inf")

for line in io.lines:
    x, op, n, _, y, cmp, t = line.split()
    regs.ensure(x, 0).ensure(y, 0)
    exec(
        f"regs['{x}'] { {'inc': '+=', 'dec': '-='}[op]} {n} if regs['{y}'] {cmp} {t} else 0"
    )
    m = max(m, regs[x])

print(m)
