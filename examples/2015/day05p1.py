from aoc import *

import re

io.lines.countby(
    lambda x: re.search(r"([aeiou].*){3,}", x)
    and re.search(r"(.)\1", x)
    and not re.search("ab|cd|pq|xy", x)
).print()
