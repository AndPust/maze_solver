from point import Point
from line import Line

class Cell(object):
    def __init__(self, up=True, down=True, left=True, right=True,
                 x1=0, x2=0, y1=0, y2=0, finish=False, visited=False):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.visited = visited

        self.w_left = Line(Point(x1,y1), Point(x1,y2))
        self.w_down = Line(Point(x1,y2), Point(x2,y2))
        self.w_up = Line(Point(x1,y1), Point(x2,y1))
        self.w_right = Line(Point(x2,y1), Point(x2,y2))

        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

        self.finish = finish

    def draw(self, canvas):

        self.w_up.draw(canvas, "black" if self.up else "#d9d9d9")
        self.w_down.draw(canvas, "black" if self.down else "#d9d9d9")
        self.w_left.draw(canvas, "black" if self.left else "#d9d9d9")
        self.w_right.draw(canvas, "black" if self.right else "#d9d9d9")
    
    def draw_move(self, canvas, to_cell, undo=False):
        colour = "red" if not undo else "gray"

        mid1 = (self.p1 + self.p2) // 2
        mid2 = (to_cell.p1 + to_cell.p2) // 2

        Line(mid1, mid2).draw(canvas, colour)
    
    def __repr__(self):
        s = ""
        if self.up:
            s += "UP "
        if self.down:
            s += "DOWN "
        if self.left:
            s += "LEFT "
        if self.right:
            s += "RIGHT "
        return s
        



