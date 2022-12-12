from aoc import *

bots = {}
bins = {}

for line in io.lines:
    a = line.split()
    if len(a) == 12:
        _, n, _, _, _, a, b, _, _, _, x, y = a

        n = int(n)
        b = int(b)
        y = int(y)

        bots.ensure(n, {})
        bots[n].ensure("values", [])
        bots[n]["lo"] = (a, b)
        bots[n]["hi"] = (x, y)
    else:
        x, y = line.ints()

        bots.ensure(y, {})
        bots[y].ensure("values", [])
        bots[y]["values"].append(x)

T = list(bots)

for n in T:
    bot = bots[n]
    if bot["values"].length > 2:
        raise RuntimeError
    if bot["values"].length == 2:
        x, y = bot["values"].sort()
        if x == 17 and y == 61:
            print(n)
            break
        for v, (t, i) in zip([x, y], [bot["lo"], bot["hi"]]):
            if t == "bot":
                bots[i]["values"].append(v)
            else:
                bins[i] = v
    else:
        T.append(n)
