from aoc import *

B = {}
B["hp"], B["atk"], B["def"] = io.data.ints()

(
    _w,
    _a,
    _r,
) = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".split(
    "\n\n"
)

w = _w.ints() % 3
a = _a.ints() % 3
r = (_r.ints() % 4).map(lambda x: x[1:])

a.append([0, 0, 0])
for _ in "  ":
    r.append([0, 0, 0])

t = []

for i1 in w:
    for i2 in a:
        for i3, i4 in r.combinations(2):
            p = {"hp": 100}
            c, p["atk"], p["def"] = i1.v + i2 + i3 + i4
            b = dict(B.items())
            while True:
                b["hp"] -= max(p["atk"] - b["def"], 1)
                if b["hp"] <= 0:
                    break
                p["hp"] -= max(b["atk"] - p["def"], 1)
                if p["hp"] <= 0:
                    t.append(c)
                    break

print(max(t))
