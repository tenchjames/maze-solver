from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry(f"{width}x{height}+0+0")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg='white', width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, line, fill='black'):
        line.draw(self.canvas, fill)
