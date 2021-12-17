from Grid import Grid


class DistanceGrid(Grid):
    def __init__(self, rows, columns):
        Grid.__init__(self, rows, columns)
        self.distances = None

    def contents_of(self, cell):
        if self.distances and cell in self.distances.cells:
            return "{}".format(self.distances[cell])
        else:
            return "X"
