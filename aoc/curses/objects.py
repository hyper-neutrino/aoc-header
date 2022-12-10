from ..utils import as_curse, list_like


@as_curse(object, "print")
def _(self, *, end="\n"):
    return self.invoke(print, end=end)


@as_curse(object, "invoke")
def _(self, f, *args, **kwargs):
    f(self, *args, **kwargs)
    return self


@as_curse(object, "starinvoke")
def _(self, f, *args, **kwargs):
    f(*self, *args, **kwargs)
    return self


@as_curse(object, "call")
def _(self, f, *args, **kwargs):
    return f(self, *args, **kwargs)


@as_curse(object, "starcall")
def _(self, f, *args, **kwargs):
    return f(*self, *args, **kwargs)


@as_curse(object, "as_list")
def _(self):
    return [x.as_list() for x in self] if type(self) in list_like else self


@as_curse(object, "minwith")
def _(self, x):
    return min(self, x)


@as_curse(object, "maxwith")
def _(self, x):
    return max(self, x)


@as_curse(object, "selfie")
def _(self, f):
    return f(self, self)
