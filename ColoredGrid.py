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

        distance = self.distances[cell]
        if distance:
            intensity = (self.max_distance - distance) / self.max_distance
            bright = int(255 * intensity)
            return QColor(bright, bright, bright)
        else:
            return QColor(0, 0, 0)
