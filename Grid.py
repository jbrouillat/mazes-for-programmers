from Cell import Cell
import random
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt, QRect


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        all_cells = []
        for row in range(self.rows):
            column_cells = []
            for column in range(self.columns):
                cell = Cell(0, column)
                column_cells.append(cell)
            all_cells.append(column_cells)
        return all_cells

    def configure_cells(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self[row, column].north = self[row - 1, column]
                self[row, column].south = self[row + 1, column]
                self[row, column].west = self[row, column - 1]
                self[row, column].east = self[row, column + 1]

    def __getitem__(self, tup):
        row, column = tup
        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return None
        return self.grid[row][column]

    def get_random_cell(self):
        row = random.randrange(0, self.rows)
        column = random.randrange(0, self.columns)
        return self[row, column]

    def each_row(self):
        for row in self.grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                cell = cell if cell is not None else Cell(-1, -1)

                # body = "   "
                body = "{:^3}".format(self.contents_of(cell))
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n"
            output += bottom + "\n"
        return output

    def paint(self, painter, x_start, y_start, cell_width, cell_height, font_size):
        white_pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(white_pen)
        painter.setRenderHint(QPainter.Antialiasing)

        font = painter.font()
        font.setPixelSize(font_size)
        painter.setFont(font)

        for mode in ["background", "wall"]:
            if mode == "wall":
                painter.drawLine(x_start, y_start, x_start + self.columns * cell_width, y_start)
            for row_index, row in enumerate(self.each_row()):
                y = y_start + row_index * cell_height
                if mode == "wall":
                    painter.drawLine(x_start, y, x_start, y + cell_height)

                for column_index, cell in enumerate(row):
                    cell = cell if cell is not None else Cell(-1, -1)

                    x = x_start + column_index * cell_width

                    # painter.drawText()
                    rectangle = QRect(x, y, cell_width, cell_height)

                    previous_brush = painter.brush()
                    previous_background = painter.background()
                    cell_color = self.background_color_for(cell)

                    if mode == "background":
                        if cell_color:
                            previous_pen = painter.pen()
                            painter.setPen(Qt.NoPen)
                            painter.setBrush(QBrush(cell_color, Qt.SolidPattern))
                            painter.drawRect(rectangle)
                            painter.setPen(previous_pen)
                            painter.setBrush(previous_brush)
                    else:
                        if cell_color:
                            painter.setBackground(cell_color)
                        painter.drawText(rectangle, Qt.AlignCenter, self.contents_of(cell))
                        if cell_color:
                            painter.setBackground(previous_background)
                        # painter.drawRect(rectangle.adjusted(2, 2, -2, -2))

                    # painter.drawLine(x, y, x, y + cell_height)
                    # painter.drawLine(x, y, x + cell_width, y)
                    # painter.drawLine(x, y + cell_height, x + cell_width, y + cell_height)
                    # painter.drawLine(x + cell_width, y, x + cell_width, y + cell_height)

                    if not cell.is_linked(cell.east):
                        painter.drawLine(x + cell_width, y, x + cell_width, y + cell_height)

                    if not cell.is_linked(cell.south):
                        painter.drawLine(x, y + cell_height, x + cell_width, y + cell_height)

    def contents_of(self, cell):
        return ""

    def background_color_for(self, cell):
        return QColor(0, 0, 0)
