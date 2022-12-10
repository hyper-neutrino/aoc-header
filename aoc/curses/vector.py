from ..utils import list_like


def vec2(f):
    def _(x, y):
        if type(x) in list_like:
            x = list(x)
        if type(y) in list_like:
            y = list(y)

        if isinstance(x, list):
            if isinstance(y, list):
                length = min(len(x), len(y))
                return ([_(a, b) for a, b in zip(x, y)] + x[length:] + y[length:]).v
            else:
                return [_(a, y) for a in x].v
        else:
            if isinstance(y, list):
                return [_(x, a) for a in y].v
            else:
                return f(x, y)

    return _


class vector(list):
    def __init__(self, x):
        self.x = [vector(k) if type(k) in list_like else k for k in x]
        list.__init__(self, self.x)

    def __add__(self, other):
        return vec2(lambda x, y: x + y)(self, other)

    def __sub__(self, other):
        return vec2(lambda x, y: x - y)(self, other)

    def __mul__(self, other):
        return vec2(lambda x, y: x * y)(self, other)

    def __div__(self, other):
        return vec2(lambda x, y: x / y)(self, other)

    def __mod__(self, other):
        return vec2(lambda x, y: x % y)(self, other)

    def __pow__(self, other):
        return vec2(lambda x, y: x**y)(self, other)

    def __floordiv__(self, other):
        return vec2(lambda x, y: x // y)(self, other)

    def __eq__(self, other):
        return vec2(lambda x, y: x == y)(self, other)

    def __ne__(self, other):
        return vec2(lambda x, y: x != y)(self, other)

    def __gt__(self, other):
        return vec2(lambda x, y: x > y)(self, other)

    def __lt__(self, other):
        return vec2(lambda x, y: x < y)(self, other)

    def __ge__(self, other):
        return vec2(lambda x, y: x >= y)(self, other)

    def __le__(self, other):
        return vec2(lambda x, y: x <= y)(self, other)

    def __and__(self, other):
        return vec2(lambda x, y: x & y)(self, other)

    def __or__(self, other):
        return vec2(lambda x, y: x | y)(self, other)

    def __xor__(self, other):
        return vec2(lambda x, y: x ^ y)(self, other)

    def __inv__(self):
        return self.vmap(lambda x: ~x)

    def __lshift__(self, other):
        return vec2(lambda x, y: x << y)(self, other)

    def __rshift__(self, other):
        return vec2(lambda x, y: x >> y)(self, other)

    def __radd__(self, other):
        return vec2(lambda x, y: x + y)(other, self)

    def __rsub__(self, other):
        return vec2(lambda x, y: x - y)(other, self)

    def __rmul__(self, other):
        return vec2(lambda x, y: x * y)(other, self)

    def __rdiv__(self, other):
        return vec2(lambda x, y: x / y)(other, self)

    def __rmod__(self, other):
        return vec2(lambda x, y: x % y)(other, self)

    def __rpow__(self, other):
        return vec2(lambda x, y: x**y)(other, self)

    def __rfloordiv__(self, other):
        return vec2(lambda x, y: x // y)(other, self)

    def __req__(self, other):
        return vec2(lambda x, y: x == y)(other, self)

    def __rne__(self, other):
        return vec2(lambda x, y: x != y)(other, self)

    def __rgt__(self, other):
        return vec2(lambda x, y: x > y)(other, self)

    def __rlt__(self, other):
        return vec2(lambda x, y: x < y)(other, self)

    def __rge__(self, other):
        return vec2(lambda x, y: x >= y)(other, self)

    def __rle__(self, other):
        return vec2(lambda x, y: x <= y)(other, self)

    def __rand__(self, other):
        return vec2(lambda x, y: x & y)(other, self)

    def __ror__(self, other):
        return vec2(lambda x, y: x | y)(other, self)

    def __rxor__(self, other):
        return vec2(lambda x, y: x ^ y)(other, self)

    def __inv__(self):
        return self.vmap(lambda x: ~x)

    def __rlshift__(self, other):
        return vec2(lambda x, y: x << y)(other, self)

    def __rrshift__(self, other):
        return vec2(lambda x, y: x >> y)(other, self)
