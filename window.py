from tkinter import Tk, BOTH, Canvas, Label

class Window(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("MAZE SOLVER")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        # self.label = Label(text="maaan")
        # self.label.pack()

        self.canvas = Canvas(self.root, height=height, width=width)
        # print(self.canvas.winfo_height())
        # print(self.canvas.winfo_width())
        # self.canvas.create_line(0, 0, 50, 50, 200, 50, 200, 200, 50, 200, 50, 50, fill="blue", width=5)
        self.canvas.pack()

        self.running = False
    
    def draw_line(self, line, fill_colour="black"):
        line.draw(self.canvas, fill_colour)

    def redraw(self):
        # self.canvas.pack()
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
