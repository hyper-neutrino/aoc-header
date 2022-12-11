from aoc import *

import json

io.lines.map(lambda x: len(json.dumps(x)) - len(x)).sum().print()
