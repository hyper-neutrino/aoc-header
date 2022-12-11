from aoc import *

import re

p = io.data

g = 1

while True:
    p = list(p)
    p[-1] = chr(ord(p[-1]) + 1)
    i = len(p) - 1
    while p[i] > "z":
        if i == 0:
            p[0] = "a"
            p.unshift("a")
            break
        p[i] = "a"
        i -= 1
        p[i] = chr(ord(p[i]) + 1)
    p = p.join("")
    if "iol".l.any(lambda x: x in p):
        continue
    if lower.l.sliding(3).any(lambda x: x.join("") in p):
        if re.search(r"(.)\1.*(.)\2", p):
            if g:
                g = 0
            else:
                break

print(p)
