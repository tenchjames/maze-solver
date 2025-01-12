from line import Line
from point import Point


class Cell():
    def __init__(self, win):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.wall_up = True
        self.wall_down = True
        self.wall_left = True
        self.wall_right = True
        self.visited = False
        self._win = win

    def draw(self, x1, y1, x2, y2, fill='black'):
        if self._win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.wall_up:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, 'white')
        if self.wall_down:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, 'white')
        if self.wall_left:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, 'white')
        if self.wall_right:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, 'white')

    def draw_move(self, to_cell, undo=False):
        x = (self.x2 - self.x1) // 2 + self.x1
        y = (self.y2 - self.y1) // 2 + self.y1

        to_x = (to_cell.x2 - to_cell.x1) // 2 + to_cell.x1
        to_y = (to_cell.y2 - to_cell.y1) // 2 + to_cell.y1
        fill = "red"
        if undo:
            fill = "gray"
        line = Line(Point(x, y), Point(to_x, to_y))
        self._win.draw_line(line, fill)
