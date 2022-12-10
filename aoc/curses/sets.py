from ..utils import as_curse


@as_curse(set, "powerset")
def _(self):
    o = set()
    for x in range(len(self) + 1):
        o |= self.combinations(x)
    return o
