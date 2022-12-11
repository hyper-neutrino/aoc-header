from aoc import *

import json


def s(x):
    if type(x) == list:
        return x.map(s).sum()
    if type(x) == dict:
        k = list(x.values())
        if "red" in k:
            return 0
        return k.map(s).sum()
    if type(x) == str:
        return 0
    return x


print(s(json.loads(io.data)))
