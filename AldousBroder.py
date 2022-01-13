import random


class AldousBroder:
    @staticmethod
    def on(grid):
        cell = grid.get_random_cell()
        unvisited = grid.size() - 1

        while unvisited > 0:
            neighbors = cell.neighbors()
            # print(cell)
            # print(",".join(str(i) for i in neighbors))

            index = random.randrange(len(cell.neighbors()))
            neighbor = cell.neighbors()[index]

            if len(neighbor.links) == 0:
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor

        return grid
