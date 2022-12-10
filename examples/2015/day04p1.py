from aoc import *

import hashlib

print(nfind(lambda i: md5(io.data + i).startswith("0" * 5)))
