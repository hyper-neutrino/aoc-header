import re
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

d2c = {">": 1, "<": -1, "^": 1j, "v": -1j}
d2p = {">": [1, 0], "<": [-1, 0], "^": [0, 1], "v": [0, -1]}

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
