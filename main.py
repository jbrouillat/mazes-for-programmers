from BinaryTreeMaze import BinaryTreeMaze
from Grid import Grid

if __name__ == '__main__':
    grid = Grid(12, 30)
    BinaryTreeMaze.on(grid)
    print(grid)
