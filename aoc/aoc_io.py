class AOC_IO:
    def __init__(self):
        self._data = None

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


io = AOC_IO()
