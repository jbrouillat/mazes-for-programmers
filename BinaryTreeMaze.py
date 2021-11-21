import random


class BinaryTreeMaze:
    @staticmethod
    def on(grid):
        for cell in grid.each_cell():
            neighbours = []
            if cell.north:
                neighbours.append(cell.north)
            if cell.east:
                neighbours.append(cell.east)

            if len(neighbours) == 0:
                continue
            
            index = random.randrange(len(neighbours))
            neighbour = neighbours[index]
            if neighbour:
                cell.link(neighbour)
