from ..utils import as_curse


@as_curse(dict, "ensure")
def _(self, key, value):
    if key not in self:
        self[key] = value
    return self
