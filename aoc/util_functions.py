import hashlib, re


def invert(f):
    return lambda *args, **kwargs: not f(*args, **kwargs)


def ints(s):
    return re.findall(r"\d+", s).map(int)


def nums(s):
    return re.findall(r"\d+(\.\d+)?", s).map(float)


def lines(s):
    return s.split("\n")


def even(x):
    if type(x) == int or type(x) == float and x % 1 == 0:
        return x % 2 == 0
    raise TypeError("can only check parity of integers")


def odd(x):
    if type(x) == int or type(x) == float and x % 1 == 0:
        return x % 2 == 1
    raise TypeError("can only check parity of integers")


def nfind(f, start=1, count=None):
    if count == 0:
        return []
    c = 1 if count is None else count
    if type(c) != int or c < 0:
        raise NotImplementedError
    o = []

    x = start
    while len(o) < c:
        if f(x):
            o.append(x)
        x += 1

    return o[0] if count is None else o


def md5(s, encoding="utf-8"):
    return hashlib.md5(bytes(s, encoding)).hexdigest()
