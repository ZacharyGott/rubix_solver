from face import Face


class Cube:

    def __init__(self, w, o, b, r, g, y):
        self.white = Face(w, 0)
        self.orange = Face(o, 1)
        self.blue = Face(b, 2)
        self.red = Face(r, 3)
        self.green = Face(g, 4)
        self.yellow = Face(y, 5)

        self.white.set_neighbors(up=self.blue, down=self.green, left=self.orange, right=self.red)
        self.orange.set_neighbors(up=self.yellow, down=self.white)
        pass

    def set_neighbors(self):
        pass

    def print_cube(self):
        r = ''
        for i in range(6):
            pass
        pass

    def rotate(self, side, rot=1):
        """
        rotate specified face by a rot multiple of 90 degrees counter clockwise
        rot=3 is equivalent to one 90 degree rotation
        """

