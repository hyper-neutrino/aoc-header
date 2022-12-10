from ..utils import as_curse
from ..util_functions import ints, nums, lines


@as_curse(str, "ints")
def _(self):
    return ints(self)


@as_curse(str, "nums")
def _(self):
    return nums(self)


@as_curse(str, "lines")
def _(self):
    return lines(self)


@as_curse(str, "list")
def _(self):
    return list(self)


@as_curse(str, "length")
@property
def _(self):
    return len(self)


@as_curse(str, "ord")
def _(self):
    return list(map(ord, self))


@as_curse(str, "tl")
def _(self, x, y=None):
    return self.list().tl(x, y)


@as_curse(str, "__mul__")
@as_curse(str, "repeat")
def _(self, other):
    if type(other) in [int, float]:
        return (
            "".join(self for _ in range(int(other)))
            + self[: int(other % 1 * len(self))]
        )
    return NotImplemented


@as_curse(str, "__add__")
def _(self, other):
    return "".join([self, str(other)])
