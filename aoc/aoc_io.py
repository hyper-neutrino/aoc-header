class AOC_IO:
    def __init__(self):
        self._data = None
        self._grid = None

    @property
    def raw(self):
        if self._data is None:
            self._data = open(0).read()
        return self._data

    @property
    def data(self):
        return self.raw.strip("\n")

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


io = AOC_IO()
