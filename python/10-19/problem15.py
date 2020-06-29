import numpy as np


class grid:

    def __init__(self, grid_size):
        self.map = np.zeros( (grid_size + 1, grid_size + 1), dtype=int )
        self.map[0] = np.ones( (1, grid_size + 1), dtype=int )
        self.map[:,0] = np.ones( (1, grid_size + 1), dtype=int )

    def print_grid(self):
        print(self.map)

    def solve_grid(self):

        for y in range(1, len(self.map)):
            for x in range(1, len(self.map)):
                if (self.map[y][x] == 0):
                    number = self.map[y-1][x] + self.map[y][x-1]
                    self.map[y][x] = number
                    self.map[x][y] = number

    def print_solution(self):
        print( self.map[-1][-1] )
            

obj = grid(20)
obj.solve_grid()
obj.print_solution()
