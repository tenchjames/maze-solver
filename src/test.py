import unittest
from maze import Maze


class TestMaze(unittest.TestCase):

    def test_initialization(self):
        maze = Maze(0, 0, 10, 10, 20, 30, None)
        self.assertEqual(maze.num_rows, 10)
        self.assertEqual(maze.num_cols, 10)
        self.assertEqual(maze.cell_size_x, 20)
        self.assertEqual(maze.cell_size_y, 30)

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_has_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        top_left_cell_has_wall_up = m1.cells[0][0].wall_up
        top_left_cell_has_wall_left = m1.cells[0][0].wall_left

        self.assertTrue((top_left_cell_has_wall_up and not top_left_cell_has_wall_left) or (
            not top_left_cell_has_wall_up and top_left_cell_has_wall_left))

        bottom_right_cell_has_wall_down = m1.cells[num_cols -
                                                   1][num_rows - 1].wall_down
        bottom_right_cell_has_wall_right = m1.cells[num_cols -
                                                    1][num_rows - 1].wall_right
        self.assertTrue((bottom_right_cell_has_wall_down and not bottom_right_cell_has_wall_right) or (
            not bottom_right_cell_has_wall_down and bottom_right_cell_has_wall_right))

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        m1.cells[0][0].visited = True
        m1._reset_visited()
        self.assertFalse(m1.cells[0][0].visited)


if __name__ == '__main__':
    unittest.main()
