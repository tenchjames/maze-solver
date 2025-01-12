from cell import Cell
import random
import time

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.cells = []
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()
        self.solve()

    def solve(self):
        self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()
        cell = self.cells[i][j]
        cell.visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        self._draw_cell(i, j)
        for k in range(4):
            x = i + directions[k][0]
            y = j + directions[k][1]
            if x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows and not self.cells[x][y].visited:
                other_cell = self.cells[x][y]
                if k == 0 and not cell.wall_up:
                    cell.draw_move(other_cell)
                    if self.solve_r(x, y):
                        return True
                elif k == 1 and not cell.wall_down:
                    cell.draw_move(other_cell)
                    if self.solve_r(x, y):
                        return True
                elif k == 2 and not cell.wall_left:
                    cell.draw_move(other_cell)
                    if self.solve_r(x, y):
                        return True
                elif k == 3 and not cell.wall_right:
                    cell.draw_move(other_cell)
                    if self.solve_r(x, y):
                        return True
                else:
                    cell.draw_move(other_cell, True)
        return False

    def _create_cells(self):
        for i in range(self.num_cols):
            cols = []
            self.cells.append(cols)
            for j in range(self.num_rows):
                cell = Cell(self._win)
                cols.append(cell)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = self.cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        top_left_cell = self.cells[0][0]
        bottom_right_cell = self.cells[self.num_cols - 1][self.num_rows - 1]
        if random.randint(0, 1) == 0:
            top_left_cell.wall_up = False
        else:
            top_left_cell.wall_left = False
        self._draw_cell(0, 0)
        # bottom wall
        if random.randint(0, 1) == 0:
            bottom_right_cell.wall_down = False
        else:
            bottom_right_cell.wall_right = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        # if the cell is not visited, mark it as visited and break the walls
        if not self.cells[i][j].visited:
            self.cells[i][j].visited = True
            self._draw_cell(i, j)
            # break the walls
            while True:
                possible_directions = []
                for k in range(4):
                    x = i + directions[k][0]
                    y = j + directions[k][1]
                    if x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows and not self.cells[x][y].visited:
                        possible_directions.append(k)
                # get a random direction
                if len(possible_directions) == 0:
                    break
                direction = random.randint(0, len(possible_directions) - 1)
                x = i + directions[possible_directions[direction]][0]
                y = j + directions[possible_directions[direction]][1]
                # break the wall between the current cell and the next cell
                if possible_directions[direction] == 0:
                    self.cells[i][j].wall_up = False
                    self.cells[x][y].wall_down = False
                elif possible_directions[direction] == 1:
                    self.cells[i][j].wall_down = False
                    self.cells[x][y].wall_up = False
                elif possible_directions[direction] == 2:
                    self.cells[i][j].wall_left = False
                    self.cells[x][y].wall_right = False
                elif possible_directions[direction] == 3:
                    self.cells[i][j].wall_right = False
                    self.cells[x][y].wall_left = False

                self._draw_cell(i, j)
                self._draw_cell(x, y)
                self._break_walls_r(x, y)

    def _reset_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False
    
