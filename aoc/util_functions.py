import hashlib, math, re
from .ocr_data import *


def invert(f):
    return lambda *args, **kwargs: not f(*args, **kwargs)


def ints(s):
    return re.findall(r"-?\d+", s).map(int)


def nums(s):
    return re.findall(r"-?\d+(\.\d+)?", s).map(float)


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


def nfind(f, start=1, count=None, tf=None):
    if count == 0:
        return []
    c = 1 if count is None else count
    if type(c) != int or c < 0:
        raise NotImplementedError
    o = []

    x = start
    while len(o) < c:
        q = x if tf is None else tf(x)
        if f(q):
            o.append(q)
        x += 1

    return o[0] if count is None else o


def md5(s, encoding="utf-8"):
    return hashlib.md5(bytes(s, encoding)).hexdigest()


def rle(x, flat=False, flip=False):
    o = []
    l = None
    for k in x:
        if l != k:
            l = k
            if flat:
                o += [1, k] if flip else [k, 1]
            else:
                o.append([1, k] if flip else [k, 1])
        else:
            if flat:
                if flip:
                    o[-2] += 1
                else:
                    o[-1] += 1
            else:
                if flip:
                    o[-1][0] += 1
                else:
                    o[-1][1] += 1
    return o


def rld(x):
    return sum([[a] * b for a, b in x], [])


def intpart(x, l):
    assert type(x) == int
    assert type(l) == int
    assert x >= 0
    assert l > 0

    if l == 1:
        return [[x]]

    return [[i, *j] for i in range(x + 1) for j in intpart(x - i, l - 1)]


def product(x, initial=1):
    t = initial
    for k in x:
        t *= k
    return t


_pyrange = range


def range(*a):
    return list(_pyrange(*a))


_pyzip = zip


def zip(*a):
    return list(map(list, _pyzip(*a)))


def map(f, a):
    return [f(x) for x in a]


def enumerate(a):
    return [(i, a[i]) for i in range(len(a))]


def ocr(x, fg="#", bg="."):
    if len(x) not in [6, 10]:
        raise ValueError("OCR only works on 6- or 10-high screens.")

    letters = {6: letters_6, 10: letters_10}[len(x)]

    if x.map(len).s.length > 1:
        raise ValueError("OCR only works on fixed-width screens.")

    if not len(x[0]):
        raise ValueError("OCR called on blank screen.")

    if x.any(lambda y: y.any(lambda z: z != fg and z != bg)):
        raise ValueError("OCR must be used on screen with only FG/BG.")

    o = ""

    while True:
        if not x.any():
            return o

        if all(r[0] == bg for r in x):
            x = [k[1:] for k in x]
            continue

        for letter in letters:
            if all(
                all(a == {"#": fg, ".": bg}[b] for a, b in zip(k, y))
                for k, y in zip(x, letter[1:])
            ):
                o += letter[0]
                x = [k[len(y) :] for k, y in zip(x, letter[1:])]
                break
        else:
            raise ValueError("OCR could not read your data.")


# https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/


def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


def crt(m, x):
    while len(x) > 1:
        t1 = modinv(m[1], m[0]) * x[0] * m[1] + modinv(m[0], m[1]) * x[1] * m[0]
        t2 = m[0] * m[1]

        x = [t1 % t2] + x[2:]
        m = [t2] + m[2:]
    return x[0]


def josephus(x, k):
    if x == 1:
        return 1
    if k == 2:
        return ~(2 ** int(math.log(x << 1, 2))) & ((x << 1) | 1)
    j = 1
    for i in range(2, x + 1):
        j = (j + k - 1) % i + 1
    return j