from aoc import *

print(
    nfind(lambda x: x.startswith("0" * 5), count=8, tf=lambda x: md5(io.data + x))
    .map(lambda x: x[5])
    .join("")
)
