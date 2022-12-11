from ..utils import as_curse


function = type(lambda: 0)


@as_curse(function, "__and__")
def _(self, x):
    def _(x):
        def f(*a, **k):
            o = []
            p = a.l
            for q in x:
                if q is None:
                    if p:
                        o.append(p.pop(0))
                else:
                    o.append(q)
            o += p
            return self(*o, **k)

        return f

    return _(x if type(x) == tuple else (x,))
