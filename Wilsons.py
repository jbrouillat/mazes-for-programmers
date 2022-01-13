import random


class Wilsons:
    @staticmethod
    def on(grid):
        unvisited = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        index = random.randrange(len(unvisited))
        first = unvisited[index]

        unvisited.remove(first)

        while len(unvisited) != 0:
            index = random.randrange(len(unvisited))
            cell = unvisited[index]
            path = [cell]

            while cell in unvisited:
                # print("current_cell:", cell)
                # print("current_path:", ", ".join(str(i) for i in path))

                # print("neighbors: ", ", ".join(str(i) for i in cell.neighbors()))
                # neighbors: list = cell.neighbors()
                # cell = random.sample(neighbors, 1)[0]

                neighbors, weights = cell.neighbors_weighted()
                cell = random.choices(neighbors, weights)[0]

                # cell = random.choices(neighbors, weights)[0]

                # print("next_cell:", cell)

                if cell in path:
                    # print("long_path: ", ", ".join(str(i) for i in path))
                    position = path.index(cell)
                    path = path[0:position + 1]
                    # print("short_path: ", ", ".join(str(i) for i in path))
                else:
                    path.append(cell)

                # print("next_path:", ", ".join(str(i) for i in path))
                # print("-")

            for index in range(0, len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])

        return grid
