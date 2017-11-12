class Group:
    def __init__(self, cells, w):
        self.cells = cells
        self.w = w

    def __str__(self):
        return "{} : {}".format(self.w, self.cells)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.w == other.w and self.cells == other.cells

    def size(self):
        return len(self.cells)

    def subtract(self, other):
        self.w -= other.w
        self.cells -= other.cells

    def all_mines(self):
        return len(self.cells) == self.w

    def all_not_mines(self):
        return self.w == 0
