from ..utils import as_curse


def intify(x):
    if x % 1 == 0:
        return int(x)
    return x


@as_curse(complex, "ri")
@property
def _(self):
    return [self.real, self.imag].map(intify)


@as_curse(complex, "ir")
@property
def _(self):
    return [self.imag, self.real].map(intify)
