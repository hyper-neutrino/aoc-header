class AOC_IO:
    def __init__(self):
        self._data = None
        self._floats = None
        self._grid = None
        self._ints = None

    @property
    def raw(self):
        if self._data is None:
            self._data = open(0).read()
        return self._data

    @property
    def data(self):
        return self.raw.strip("\n")

    @property
    def blocks(self):
        return self.data.split("\n\n")

    @property
    def lines(self):
        return self.data.splitlines()

    @property
    def grid(self):
        if self._grid is None:
            self._grid = self.lines.map(list)
            length = self._grid.map(len).max()
            self._grid = [row + [" "] * (length - len(row)) for row in self._grid]
        return self._grid

    @property
    def ints(self):
        if self._ints is None:
            self._ints = self.data.ints()
        return self._ints

    @property
    def floats(self):
        if self._floats is None:
            self._floats = self.data.floats()
        return self._floats


io = AOC_IO()
