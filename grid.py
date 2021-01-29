from cell import Cell


class Grid:

    def __init__(self, size):
        self.grid = []
        self.floors = []
        for i in range(0, size):
            row = []
            for j in range(0, size):
                cell_type = "wall"
                if not (1 < i < 5 and j == 2 or 0 < j < 6 and i == 1 or i == 2 and j == 4 or
                        4 < j < 10 and i == 6 or 3 < i < 7 and j == 5 or
                        5 < i < 9 and j == 1 or 1 < j < 6 and i == 8 or
                        0 < i < 5 and 6 < j < 8 or j == 8 and 5 < i < 9 or i == 2 and j == 8 or i == 4 and j == 9 or
                        i == 6 and 1 < j < 4 or i == 4 and j == 3 or i == 3 and j == 0 or i == 0 and j == 7):
                    cell_type = "floor"
                    self.floors.append([i, j])
                new_cell = Cell(i, j, cell_type)
                row.append(new_cell)
            self.grid.append(row)

    def draw(self, canvas, resource, image_size):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.grid[i][j].draw(canvas, resource, image_size)
