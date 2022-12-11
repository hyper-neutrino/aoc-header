from aoc import *


lines = io.lines.map(lambda x: x.split(" -> "))


def _eval(x):
    if x.isdigit():
        return int(x)
    if " " not in x:
        return s[x]
    if x.startswith("NOT"):
        return 65535 - _eval(x[4:])
    x = x.split()
    return {
        "AND": band_,
        "OR": bor_,
        "LSHIFT": lambda x, y: (x << y) % 65536,
        "RSHIFT": rshift_,
    }[x[1]](_eval(x[0]), _eval(x[2]))


s = {}


for a, b in lines:
    try:
        s[b] = _eval(a)
    except:
        lines.append([a, b])

print(s["a"])
