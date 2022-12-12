from aoc import *

s = [" "] * 8

i = 0
while " " in s:
    h = md5(io.data + i)
    if h.startswith("0" * 5):
        if "0" <= h[5] <= "7":
            n = int(h[5])
            if s[n] == " ":
                s[n] = h[6]
    i += 1

print(s.join(""))
