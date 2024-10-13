from window import Window
from line import Line
from point import Point
from cell import Cell

import time

def main():
    win = Window(800, 600)
    win.root.minsize(800, 600)

    midx = 400
    midy = 300

    l0 = Line(Point(0, 0), Point(400, 600))
    l1 = Line(Point(0, 0), Point(800, 600))
    # l2 = Line(Point(midx, midy - 50), Point(midx, midy - 150))
    # l3 = Line(Point(midx, midy + 50), Point(midx, midy + 150))
    # l4 = Line(Point(midx - 50, midy), Point(midx - 150, midy))

    l0.draw(win.canvas, "red")
    l1.draw(win.canvas)
    # l2.draw(win.canvas)
    # l3.draw(win.canvas)
    # l4.draw(win.canvas)

    c1 = Cell(x1=50, x2=100, y1=150, y2=200)
    c2 = Cell(x1=150, x2=200, y1=150, y2=200, up=False, right=False)

    c1.draw(win.canvas)
    c2.draw(win.canvas)

    c1.draw_move(win.canvas, c2)

    win.redraw()

    time.sleep(3)

    c1.draw_move(win.canvas, c2, True)

    win.redraw()

    win.wait_for_close()


if __name__ == "__main__":
    main()