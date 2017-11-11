class Group:
    def __init__(self, cells, w):
        self.cells = cells
        self.w = w

    def __str__(self):
        return "{} : {}".format(self.w, self.cells)

    def __repr__(self):
        return self.__str__()

    def size(self):
        return len(self.cells)
