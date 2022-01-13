from Distances import Distances


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.links = []

    def link(self, cell, bidirectional=True):
        self.links.append(cell)
        if bidirectional:
            cell.link(self, bidirectional=False)

    def unlink(self, cell, bidirectional=True):
        self.links.remove(cell)
        if bidirectional:
            cell.unlink(self, bidirectional=False)

    def is_linked(self, cell):
        return cell in self.links

    def neighbors(self) -> list:
        n = []
        if self.north is not None:
            n.append(self.north)
        if self.south is not None:
            n.append(self.south)
        if self.west is not None:
            n.append(self.west)
        if self.east is not None:
            n.append(self.east)
        return n

    def neighbors_weighted(self) -> (list, list):
        n = []
        w = []
        if self.north is not None:
            n.append(self.north)
            w.append(1)
        if self.south is not None:
            n.append(self.south)
            w.append(1)
        if self.west is not None:
            n.append(self.west)
            w.append(1)
        if self.east is not None:
            n.append(self.east)
            w.append(1)
        return n, w

    def __str__(self):
        return "Cell(" + str(self.row) + ", " + str(self.column) + ")"

    def distances(self):
        distances = Distances(self)
        frontier = [self]

        while len(frontier) != 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links:
                    if linked_cell in distances.cells:
                        continue
                    # print(cell)
                    distances[linked_cell] = distances[cell] + 1
                    new_frontier.extend(cell.links)

            frontier = new_frontier

        return distances
