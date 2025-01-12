

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def draw(self, canvas, fill='black'):
        canvas.create_line(self.coor1.x, self.coor1.y,
                           self.coor2.x, self.coor2.y, fill=fill)
