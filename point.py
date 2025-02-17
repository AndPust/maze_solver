

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __truediv__(self, other):
        return Point(self.x/other, self.y/other)
    
    def __floordiv__(self, other):
        return Point(self.x//other, self.y//other)