import re
from collections import deque
from forbiddenfruit import curse


def as_curse(klass, name):
    def _(f):
        if type(f) == property or re.match(r"^__\w+__$", name):
            curse(klass, name, f)
        else:

            def g(*a, **k):
                v = f(*a, **k)
                if v == NotImplemented:
                    raise NotImplementedError
                return v

            curse(klass, name, g)
        return f

    return _


list_like = [list, set, tuple, enumerate, map, zip]

d2c = {}
d2p = {}

for v, c in [
    (1, ">RrEe"),
    (-1, "<LlWw"),
    (1j, "^UuNn"),
    (-1j, "vDdSs"),
    (1 + 1j, ["UR", "ur", "NE", "ne"]),
    (1 - 1j, ["DR", "dr", "SE", "se"]),
    (-1 - 1j, ["DL", "dl", "SW", "sw"]),
    (-1 + 1j, ["UL", "ul", "NW", "nw"]),
]:
    for k in c:
        d2c[k] = v
        d2p[k] = (int(v.real), int(v.imag))

h2c = {}
h2p = {}

for v, c in [
    (1 + 1j, ["UR", "ur", "NE", "ne"]),
    (1 - 1j, ["DR", "dr", "SE", "se"]),
    (-2j, "DdSs"),
    (-1 - 1j, ["DL", "dl", "SW", "sw"]),
    (-1 + 1j, ["UL", "ul", "NW", "nw"]),
    (2j, "UuNn"),
]:
    for k in c:
        h2c[k] = v
        h2p[k] = (int(v.real), int(v.imag))

add_ = lambda x, y: x + y
sub_ = lambda x, y: x - y
mul_ = lambda x, y: x * y
div_ = lambda x, y: x / y
mod_ = lambda x, y: x % y
pow_ = lambda x, y: x**y
floordiv_ = lambda x, y: x // y

eq_ = lambda x, y: x == y
ne_ = lambda x, y: x != y
gt_ = lambda x, y: x > y
lt_ = lambda x, y: x < y
ge_ = lambda x, y: x >= y
le_ = lambda x, y: x <= y

and_ = lambda x, y: x and y
or_ = lambda x, y: x or y
not_ = lambda x: not x

is_ = lambda x, y: x is y
isnot_ = lambda x, y: x is not y

in_ = lambda x, y: x in y
notin_ = lambda x, y: x not in y

band_ = lambda x, y: x & y
bor_ = lambda x, y: x | y
xor_ = lambda x, y: x ^ y
inv_ = lambda x: ~x
lshift_ = lambda x, y: x << y
rshift_ = lambda x, y: x >> y


radd_ = lambda x, y: y + x
rsub_ = lambda x, y: y - x
rmul_ = lambda x, y: y * x
rdiv_ = lambda x, y: y / x
rmod_ = lambda x, y: y % x
rpow_ = lambda x, y: y**x
rfloordiv_ = lambda x, y: y // x

req_ = lambda x, y: y == x
rne_ = lambda x, y: y != x
rgt_ = lambda x, y: y > x
rlt_ = lambda x, y: y < x
rge_ = lambda x, y: y >= x
rle_ = lambda x, y: y <= x

rand_ = lambda x, y: y and x
ror_ = lambda x, y: y or x

ris_ = lambda x, y: y is x
risnot_ = lambda x, y: y is not x

rin_ = lambda x, y: y in x
rnotin_ = lambda x, y: y not in x

rband_ = lambda x, y: y & x
rbor_ = lambda x, y: y | x
rxor_ = lambda x, y: y ^ x
ylshift_ = lambda x, y: y << x
rrshift_ = lambda x, y: y >> x

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
Aa = upper + lower
aA = lower + upper


class permutation:
    def __init__(self, x):
        assert type(x) == list and sorted(x) == list(range(len(x)))
        self.x = x

    def __repr__(self):
        return "P[" + self.x.join(", ") + "]"

    def parse(start, end):
        assert len(start) == len(end)
        s = start.l
        e = end.l
        return permutation(e.map(s.index))

    def apply(self, x):
        assert len(x) == len(self.x)
        return [x[i] for i in self.x]

    def mutate(self, x):
        x[:] = self.apply(x)
        return x

    def __mul__(self, x):
        if type(x) != permutation:
            return NotImplemented
        assert len(x.x) == len(self.x)
        return permutation([self.x[i] for i in x.x])

    def inverse(self):
        o = [None] * len(self.x)
        for i, e in enumerate(self.x):
            o[e] = i
        return permutation(o)

    def __pow__(self, x):
        assert type(x) == int

        if x == 0:
            return permutation(list(range(len(self.x))))
        if x == 1:
            return self
        if x == -1:
            return self.inverse()
        if x < 0:
            return self.inverse() ** -x

        r = permutation(list(range(len(self.x))))
        c = permutation(self.x)

        while x:
            if x & 1:
                r *= c
            x >>= 1
            c *= c

        return r
