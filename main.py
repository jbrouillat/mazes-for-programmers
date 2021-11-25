from BinaryTreeMaze import BinaryTreeMaze
from Grid import Grid

# from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter  # , QBrush, QPen
# from PyQt5.QtCore import Qt

import sys


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
        self.grid_cell_width = 20
        self.grid_cell_height = 20

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def set_grid(self, grid):
        self.grid = grid
        if self.grid is None:
            self.setGeometry(self.top, self.left, self.width, self.height)
        else:
            self.setGeometry(self.top, self.left, grid.columns * self.grid_cell_width + 2 * self.grid_x_start,
                             grid.rows * self.grid_cell_height + 2 * self.grid_y_start)

    def paintEvent(self, event):
        painter: int = QPainter(self)
        if self.grid is None:
            return

        self.grid.paint(painter, self.grid_x_start, self.grid_y_start, self.grid_cell_width, self.grid_cell_height)


def main():
    grid = Grid(30, 30)
    BinaryTreeMaze.on(grid)
    # print(grid)

    app = QApplication(sys.argv)
    window = Window()
    window.set_grid(grid)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
