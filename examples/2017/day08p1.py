from aoc import *

regs = {}

for line in io.lines:
    x, op, n, _, y, cmp, t = line.split()
    regs.ensure(x, 0).ensure(y, 0)
    exec(
        f"regs['{x}'] { {'inc': '+=', 'dec': '-='}[op]} {n} if regs['{y}'] {cmp} {t} else 0"
    )

print(max(regs.values()))
