from aoc import *

g = io.grid
p = g[0].index("|") * 1j
d = 1

t = 1

while True:
    t += 1
    p += d
    c = g.idx(p.ri)
    nr, nc = (p + d).ri
    if not len(g) > nr >= 0 <= nc < len(g[0]) or g[nr][nc] == " ":
        for nr, nc in [(p + d * 1j).ri, (p + d * -1j).ri]:
            if len(g) > nr >= 0 <= nc < len(g[0]) and g[nr][nc] != " ":
                dr, dc = [nr, nc].v - p.ri
                d = dr + dc * 1j
                break
        else:
            break

print(t)