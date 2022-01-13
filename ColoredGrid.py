from PyQt5.QtGui import QColor

from Grid import Grid


class ColoredGrid(Grid):
    def __init__(self, rows, columns):
        Grid.__init__(self, rows, columns)
        self._distances = None
        self.farthest_cell = None
        self.max_distance = None

    @property
    def distances(self):
        return self._distances

    @distances.setter
    def distances(self, distances):
        self._distances = distances
        self.farthest_cell, self.max_distance = self._distances.max_length()

    def background_color_for(self, cell):
        if self.distances is None:
            return QColor(0, 0, 0)

        distance = self.distances[cell]
        if distance is None:
            return QColor(0, 0, 0)

        intensity = (self.max_distance - distance) / self.max_distance
        dark = int(255 * intensity)
        bright = 128 + int(127 * intensity)
        return QColor(dark, bright, dark)

    # def contents_of(self, cell):
    #     if self.distances and cell in self.distances.cells:
    #         return "{}".format(self.distances[cell])
    #     else:
    #         return ""
