from typing import Any


class Distances:
    cells: dict[Any, int]

    def __init__(self, root: Any):
        self.root = root
        self.cells = {self.root: 0}

    def __getitem__(self, cell):
        if cell in self.cells:
            return self.cells[cell]
        else:
            return None

    def __setitem__(self, cell, distance):
        self.cells[cell] = distance
