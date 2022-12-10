from aoc import *

import re

io.lines.countby(lambda x: re.search(r"(..).*\1", x) and re.search(r"(.).\1", x)).print()
