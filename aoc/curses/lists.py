import itertools, types

from .vector import vector
from ..utils import as_curse, list_like
from ..util_functions import product, xrange

_list_sort = list.sort


def tl_pass(o, x, y):
    fx = type(x) == types.FunctionType
    fy = type(y) == types.FunctionType

    if fx:
        if fy:
            return [y(k) if x(k) else k for k in o]
        else:
            return [y if x(k) else k for k in o]
    else:
        if fy:
            return [y(k) if x == k else k for k in o]
        else:
            return [y if x == k else k for k in o]


def vtl_pass(o, x, y):
    fx = type(x) == types.FunctionType
    fy = type(y) == types.FunctionType

    r = []

    for k in o:
        if type(k) in list_like:
            r.append(type(k)(vtl_pass(k, x, y)))
        elif x(k) if fx else k == x:
            r.append(y(k) if fy else y)
        else:
            r.append(k)

    return r


@as_curse(list, "shift")
def _(self):
    return self.pop(0)


@as_curse(list, "unshift")
def _(self, value):
    self.insert(0, value)
    return value


@as_curse(list, "rm")
def _(self, i):
    self.pop(i)
    return self


@as_curse(list, "prepend")
def _(self, value):
    self.insert(0, value)
    return self


@as_curse(list, "sort")
def _(self, *, key=None, reverse=False):
    _list_sort(self, key=key, reverse=reverse)
    return self


@as_curse(list, "reverse")
def _(self):
    self[:] = self[::-1]
    return self


@as_curse(list, "swap")
def _(self, x, y):
    self[x], self[y] = self[y], self[x]


for tp in [list, tuple]:

    def _(tp):
        @as_curse(tp, "sortq")
        def _(self, *, key=None, reverse=False):
            if len(self) < 2:
                return True
            k = self[0] if key is None else key(self[0])
            for i in xrange(1, len(self)):
                n = self[i] if key is None else key(self[i])
                if n > k if reverse else n < k:
                    return False
                k = n
            return True

    _(tp)


for tp in [list, tuple, set]:

    def _(tp):
        tp2 = tuple if tp == set else tp

        @as_curse(tp, "length")
        @property
        def _(self):
            return len(self)

        @as_curse(tp, "map")
        def _(self, f):
            return tp(map(f, self))

        @as_curse(tp, "mapsplat")
        def _(self, f):
            return tp(f(*x) for x in self)

        @as_curse(tp, "tl")
        def _(self, x, y=None):
            if y is None and type(x) != dict:
                raise RuntimeError(
                    "Translation requires either two values or a dictionary."
                )

            output = tp(self)

            if y is None:
                for x, y in x.items():
                    output = tp(tl_pass(output, x, y))
            else:
                output = tp(tl_pass(output, x, y))

            return output

        @as_curse(tp, "vtl")
        def _(self, x, y=None):
            if y is None and type(x) != dict:
                raise RuntimeError(
                    "Translation requires either two values or a dictionary."
                )

            output = tp(self)

            if y is None:
                for x, y in x.items():
                    output = tp(vtl_pass(output, x, y))
            else:
                output = tp(vtl_pass(output, x, y))

            return output

        @as_curse(tp, "filter")
        def _(self, f=lambda x: x):
            return tp(x for x in self if f(x))

        @as_curse(tp, "filtersplat")
        def _(self, f=any):
            return tp(x for x in self if f(*x))

        @as_curse(tp, "filterout")
        def _(self, f=lambda x: x):
            return tp(x for x in self if not f(x))

        @as_curse(tp, "filteroutsplat")
        def _(self, f=all):
            return tp(x for x in self if not f(*x))

        if tp != set:

            @as_curse(tp, "sorted")
            def _(self, *, key=None, reverse=False):
                return tp(sorted(self, key=key, reverse=reverse))

            @as_curse(tp, "reduce")
            def _(self, f, initial=None):
                if initial is None:
                    if len(self) > 0:
                        value = self[0]
                    else:
                        raise RuntimeError(
                            f"Cannot reduce empty list without an initial value."
                        )
                elif len(self) > 0:
                    value = f(initial, self[0])
                for i in range(1, len(self)):
                    value = f(value, self[i])
                return value

            @as_curse(tp, "creduce")
            def _(self, f, initial=None):
                output = [initial] if initial is not None else []
                for x in self:
                    if output:
                        output.append(f(output[-1], x))
                    else:
                        output.append(x)
                return tp(output)

            @as_curse(tp, "rreduce")
            def _(self, f, initial=None):
                return self[::-1].reduce(f, initial)

            @as_curse(tp, "crreduce")
            def _(self, f, initial=None):
                return self[::-1].creduce(f, initial)

            @as_curse(tp, "csum")
            def _(self, initial=None):
                return self.creduce(lambda x, y: x + y, initial)

            @as_curse(tp, "zipwith")
            def _(self, other):
                return tp(map(tp, zip(self, other)))

            @as_curse(tp, "zip")
            def _(self):
                return tp(map(tp, zip(*self)))

            @as_curse(tp, "__sub__")
            @as_curse(tp, "exclude")
            def _(self, other):
                if type(other) in list_like:
                    return tp(x for x in self if x not in other)
                return tp(x for x in self if x != other)

            @as_curse(tp, "__mul__")
            @as_curse(tp, "dot")
            def _(self, other):
                if type(other) in list_like:
                    if len(self) != len(other):
                        raise ValueError("dot product of uneven lists")
                    return sum(x * y for x, y in zip(self, other))
                if type(other) in [int, float]:
                    return (
                        sum([self for _ in range(int(other))], tp())
                        + self[: int(other % 1 * len(self))]
                    )
                return NotImplemented

            @as_curse(tp, "__div__")
            @as_curse(tp, "divide")
            def _(self, other=2):
                if type(other) == int:
                    if other == 0:
                        return tp(tp([x]) for x in self)

                    if other < 0:
                        return tp(x[::-1] for x in self[::-1] / -other)[::-1]

                    start = 0
                    extend = len(self) % other
                    span = len(self) // other
                    out = []

                    for _ in range(other):
                        next = start + span + (extend > 0)
                        out.append(self[start:next])
                        start = next
                        extend -= 1

                    return tp(out)
                return NotImplemented

            @as_curse(tp, "__mod__")
            @as_curse(tp, "chunks")
            def _(self, other=2):
                if type(other) == int:
                    return tp(self[i : i + other] for i in range(0, len(self), other))
                return NotImplemented

            @as_curse(tp, "__pow__")
            @as_curse(tp, "cart")
            def _(self, other):
                if type(other) in list_like:
                    return tp(tp(tp([x, y]) for y in other) for x in self)
                elif type(other) == int and other > 0:
                    if other == 1:
                        return tp(tp2([x]) for x in self)
                    return tp(tp2([x, *k]) for x in self for k in self ** (other - 1))
                return NotImplemented

            @as_curse(tp, "__floordiv__")
            @as_curse(tp, "nfurcate")
            def _(self, other=2):
                if type(other) == int:
                    if other == 0:
                        raise ZeroDivisionError("n-furcate by zero")
                    if other < 0:
                        raise ValueError("n-furcate by negative number")
                    return tp(self[i::other] for i in range(other))
                return NotImplemented

            @as_curse(tp, "sliding")
            def _(self, other=2, wrap=False):
                if type(other) != int:
                    return NotImplemented
                if other == 0:
                    return NotImplemented
                out = other < 0
                other = abs(other)
                o = []
                for i in range(len(self) if wrap else len(self) - other + 1):
                    e = i + other
                    if e > len(self):
                        if out:
                            o.append(self[e - len(self) : i])
                        else:
                            o.append(self[i:] + self[: e - len(self)])
                    else:
                        if out:
                            o.append(self[:i] + self[e:])
                        else:
                            o.append(self[i:e])
                return tp(o)

            @as_curse(tp, "__and__")
            @as_curse(tp, "intersect")
            def _(self, other):
                if hasattr(other, "__iter__"):
                    return tp(x for x in self if x in other)
                return NotImplemented

            @as_curse(tp, "__or__")
            @as_curse(tp, "interleave")
            def _(self, other):
                if type(other) in list_like:
                    other = tp(other)
                    length = min(len(self), len(other))
                    return (
                        sum([tp([x, y]) for x, y in zip(self, other)], tp())
                        + self[length:]
                        + other[length:]
                    )
                return (sum([[x, other] for x in self], []))[:-1]

            @as_curse(tp, "__xor__")
            @as_curse(tp, "mutex")
            def _(self, other):
                if type(other) in list_like:
                    other = tp(other)
                    return tp(x for x in self if x not in other) + tp(
                        x for x in other if x not in self
                    )
                return NotImplemented

            @as_curse(tp, "__lshift__")
            @as_curse(tp, "rotate")
            def _(self, other):
                if type(other) == int:
                    if self == tp():
                        return tp()
                    other %= self.length
                    return self[other:] + self[:other]
                return NotImplemented

            @as_curse(tp, "__rshift__")
            def _(self, other):
                return self << -other

            @as_curse(tp, "chr")
            def _(self):
                if not all(type(x) == int and x >= 0 for x in self):
                    raise ValueError(
                        "chr can only be used on lists of non-negative integers"
                    )
                return "".join(map(chr, self))

            @as_curse(tp, "flat")
            def _(self):
                return sum([x.flat() if type(x) == tp else tp([x]) for x in self], tp())

            @as_curse(tp, "nflat")
            def _(self, n=1):
                if n <= 0:
                    return self
                return sum(
                    [x.nflat(n - 1) if type(x) == tp else tp([x]) for x in self], tp()
                )

            @as_curse(tp, "powerset")
            def _(self):
                return tp(self.combinations(x) for x in range(len(self) + 1)).nflat(1)

        @as_curse(tp, "sum")
        def _(self, initial=0):
            return sum(self, initial)

        @as_curse(tp, "product")
        def _(self, initial=1):
            return product(self, initial)

        @as_curse(tp, "all")
        def _(self, f=lambda x: x):
            return all(f(x) for x in self)

        @as_curse(tp, "any")
        def _(self, f=lambda x: x):
            return any(f(x) for x in self)

        @as_curse(tp, "anyall")
        def _(self, f=lambda x: x):
            return self and self.all(f)

        @as_curse(tp, "vmap")
        def _(self, f):
            return tp(x.vmap(f) if hasattr(x, "vmap") else f(x) for x in self)

        @as_curse(tp, "vfilter")
        def _(self, f):
            o = []
            for x in self:
                if hasattr(x, "vfilter"):
                    o.append(x.vfilter(f))
                elif f(x):
                    o.append(x)
            return tp(o)

        @as_curse(tp, "vfilterout")
        def _(self, f):
            o = []
            for x in self:
                if hasattr(x, "vfilterout"):
                    o.append(x.vfilterout(f))
                elif not f(x):
                    o.append(x)
            return tp(o)

        @as_curse(tp, "join")
        def _(self, x=""):
            if type(x) == str:
                return x.join(map(str, self))
            return NotImplemented

        @as_curse(tp, "max")
        def _(self, *, key=None):
            return max(self, key=key)

        @as_curse(tp, "min")
        def _(self, *, key=None):
            return min(self, key=key)

        @as_curse(tp, "combinations")
        def _(self, r=2):
            return tp(map(tp2, itertools.combinations(self, r)))

        @as_curse(tp, "permutations")
        def _(self, r=None):
            return tp(map(tp2, itertools.permutations(self, r)))

        @as_curse(tp, "countby")
        def _(self, f=lambda x: bool(x)):
            return sum(map(bool, map(f, self)))

        @as_curse(tp, "minimal")
        def _(self, f=lambda x: x):
            if len(self) == 0:
                return tp()
            k = list(self)
            o = [k.pop(0)]
            m = f(o[0])
            for x in k:
                q = f(x)
                if q < m:
                    o = [x]
                    m = q
                elif q == m:
                    o.append(x)
            return tp(o)

        @as_curse(tp, "maximal")
        def _(self, f=lambda x: x):
            if len(self) == 0:
                return tp()
            k = list(self)
            o = [k.pop(0)]
            m = f(o[0])
            for x in k:
                q = f(x)
                if q > m:
                    o = [x]
                    m = q
                elif q == m:
                    o.append(x)
            return tp(o)

    _(tp)

for tp in [list, set, tuple, vector, str]:

    @as_curse(tp, "l")
    @property
    def _(self):
        return list(self)

    @as_curse(tp, "s")
    @property
    def _(self):
        return set(self)

    @as_curse(tp, "t")
    @property
    def _(self):
        return tuple(self)

    @as_curse(tp, "v")
    @property
    def _(self):
        return vector(self)

    @as_curse(tp, "idx")
    def _(self, index):
        if type(index) == int:
            return self[index % len(self)]
        if type(index) == float:
            if index % 1 == 0:
                return self[index % len(self)]
            return (self[int(index) % len(self)], self[int(index + 1) % len(self)])
        if type(index) in [list, tuple, vector]:
            if len(index) == 1:
                return self[index[0] % len(self)]
            return self[index[0] % len(self)].idx(index[1:])
        raise NotImplementedError
