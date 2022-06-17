

class Face:
    
    def __init__(self, mat, index):
        self.mat = mat
        self.index = index
        self.up = self.down = self.left = self.right = None
        pass

    def set_neighbors(self, up, down, left, right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        pass
