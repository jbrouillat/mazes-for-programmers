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

    def path_to(self, goal):
        current = goal

        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links:
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break

        return breadcrumbs

    def max_length(self):
        max_distance = 0
        max_cell = self.root

        for cell, distance in self.cells.items():
            if distance > max_distance:
                max_cell = cell
                max_distance = distance

        return [max_cell, max_distance]
