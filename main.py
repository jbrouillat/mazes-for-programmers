from typing import Union

from AldousBroder import AldousBroder
from BinaryTreeMaze import BinaryTreeMaze
from ColoredGrid import ColoredGrid
from DistanceGrid import DistanceGrid
from Grid import Grid

# from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPalette
from PyQt5.QtCore import Qt

import sys

from Wilsons import Wilsons


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "mazes-for-programmers"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.init_window()
        self.grid = None
        self.grid_x_start = 20
        self.grid_y_start = 20
        self.grid_cell_width = 10
        self.grid_cell_height = 10
        self.grid_font_size = 5

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        # self.setStyleSheet("background-color: black;")
        self.show()

    def set_grid(self, grid):
        self.grid = grid
        if self.grid is None:
            self.setGeometry(self.top, self.left, self.width, self.height)
        else:
            self.setGeometry(self.top, self.left, grid.columns * self.grid_cell_width + 2 * self.grid_x_start,
                             grid.rows * self.grid_cell_height + 2 * self.grid_y_start)

    def paintEvent(self, event):
        painter: Union[QPainter, QPainter] = QPainter(self)
        if self.grid is None:
            return

        # background_brush = QBrush(QColor(0, 0, 0), Qt.SolidPattern)
        # painter.setBackground(background_brush)
        painter.setBackground(QColor(0, 0, 0))

        painter.setClipping(True)
        painter.setBackgroundMode(Qt.BGMode.OpaqueMode)

        painter.eraseRect(self.rect())

        # pal = self.palette()
        # pal.setColor(QPalette.Background, Qt.black)
        # self.setAutoFillBackground(True)

        self.grid.paint(painter, self.grid_x_start, self.grid_y_start,
                        self.grid_cell_width, self.grid_cell_height, self.grid_font_size)


def main():
    # grid = DistanceGrid(20, 20)
    # grid = Grid(5, 5)
    grid = ColoredGrid(80, 80)

    # for cell in grid.each_cell():
    #     print("Cell:", cell)
    #     print("North:", cell.north)
    #     print("South:", cell.south)
    #     print("West:", cell.west)
    #     print("East:", cell.east)
    #     print("Neighbors: ", ", ".join(str(i) for i in cell.neighbors()))
    # return

    # BinaryTreeMaze.on(grid)
    # AldousBroder.on(grid)
    Wilsons.on(grid)

    start = grid[0, 0]
    distances = start.distances()
    # grid.distances = distances

    # Shortest path to cell
    # shortest_path = distances.path_to(grid[10, 10])
    # grid.distances = shortest_path

    # Max path in a maze
    new_start, new_distance = distances.max_length()
    new_distances = new_start.distances()
    goal, goal_distance = new_distances.max_length()
    # grid.distances = new_distances.path_to(goal)
    grid.distances = goal.distances()

    # print(", ".join(str(i) for i in distances.max_length()))

    # print(grid)

    app = QApplication(sys.argv)
    window = Window()
    window.set_grid(grid)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
