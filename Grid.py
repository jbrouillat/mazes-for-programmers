from Cell import Cell
import random


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

                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary

                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner

            output += top + "\n"
            output += bottom + "\n"

        return output
