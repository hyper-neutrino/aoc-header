from aoc import *

disks = io.data.ints() % 4
disks += [[len(disks) + 1, 11, 0, 0]]

disks.mapsplat(lambda i, m, _, x: (m, (-x - i) % m)).zip().callsplat(crt).print()
