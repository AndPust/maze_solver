from cell import Cell

import time, random

class Maze(object):
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_lists()

        if seed:
            random.seed(seed)
    
    def create_lists(self):
        self._cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j] = Cell(x1=self.x1+i*self.cell_size_x, y1=self.y1+j*self.cell_size_y,
                                         x2=self.x1+(i+1)*self.cell_size_x, y2=self.y1+(j+1)*self.cell_size_y)
        
        self.bread_entrance_and_exit()

    def draw(self):
        for col in self._cells:
            for c in col:
                c.draw(self.win.canvas)    

    def draw_cell(self, i, j):
        self._cells[i][j].draw(self.win.canvas)
    
    def animate(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i,j)
                self.win.redraw()
                time.sleep(0.01)
    
    def bread_entrance_and_exit(self):
        self._cells[0][0].up = False
        # self.draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].down = False
        # self.draw_cell(self.num_cols-1, self.num_rows-1)
        
    def break_walls(self, i, j, side=None):
        print(f"VISITING: {i} : {j}")

        self._cells[i][j].visited = True

        def the_other_side(s):
            match s:
                case "left":
                    return "right"
                case "right":
                    return "left"
                case "up":
                    return "down"
                case "down":
                    return "up"
                case _:
                    pass

        def left():
            print("AAAA!1")
            self._cells[i][j].left = False
        def right():
            print("AAAA!2")
            self._cells[i][j].right = False
        def up():
            print("AAAA!3")
            self._cells[i][j].up = False
        def down():
            print("AAAA!4")
            self._cells[i][j].down = False
        
        matcher = {
                "left":left,
                "right":right,
                "up":up,
                "down":down,
        }

        print(f"SIDEE: {side}")
        if side:
            matcher[side]()

        print(self._cells[i][j])

        while True:
            li = []
            if i != 0 and not self._cells[i-1][j].visited:
                li.append((i-1,j,"right"))
            if j != 0 and not self._cells[i][j-1].visited:
                li.append((i,j-1,"down"))
            if i != self.num_cols-1 and not self._cells[i+1][j].visited:
                li.append((i+1,j,"left"))
            if j != self.num_rows-1 and not self._cells[i][j+1].visited:
                li.append((i,j+1,"up"))

            if len(li) == 0:
                # self._cells[i][j].draw(self.win.canvas)
                self.win.redraw()
                # time.sleep(0.01)
                print(f"NO MORE TO VISIT FROM: {i} : {j}")
                print(self._cells[i][j])
                return

            random.shuffle(li)

            p = li[0]
            setattr(self._cells[i][j], the_other_side(p[2]), False)
            # self._cells[i][j].draw(self.win.canvas)
            self.win.redraw()
            # time.sleep(0.01)
            self.break_walls(p[0], p[1], p[2])
    
    def reset_cells_visited(self):
        for r in self._cells:
            for c in r:
                c.visited = False





        