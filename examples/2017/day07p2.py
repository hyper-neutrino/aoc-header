from aoc import *

w = {}
c = {}

e = set()

for line in io.lines:
    n = line.split()[0]
    w[n] = line.ints()[0]
    if "->" in line:
        line, r = line.split(" -> ")
        o = r.split(", ")
        e |= set(o)
        c[n] = o


(k,) = set(w) - e

s = {}


def f(k):
    s[k] = c[k].map(f).sum() + w[k] if k in c else w[k]
    return s[k]


f(k)


l = -1

while True:
    e = c[k].map(lambda x: (x, s[x]))
    f = e.map(lambda x: x[1])
    e.sort(key=lambda x: f.count(x[1]))
    if e[0][1] == e[1][1]:
        print(w[k] - s[k] + l)
        break
    k = e[0][0]
    l = e[1][1]
