from face import Face
import numpy as np


class Cube:

    def __init__(self, w, o, b, r, g, y):
        self.white = w
        self.orange = o
        self.blue = b
        self.red = r
        self.green = g
        self.yellow = y

    def print_cube(self):
        r = ''

        # Print yellow
        for i in range(3):
            for n in range(3):
                r += (self.yellow[i][n])
            r += '\n'

        # Middle four
        for i in range(3):
            r += self.orange[i][0]
            r += self.orange[i][1]
            r += self.orange[i][2]
            r += ' '

            r += self.blue[i][0]
            r += self.blue[i][1]
            r += self.blue[i][2]
            r += ' '

            r += self.red[i][0]
            r += self.red[i][1]
            r += self.red[i][2]
            r += ' '

            r += self.green[i][0]
            r += self.green[i][1]
            r += self.green[i][2]

            r += '\n'

        # Print white
        for i in range(3):
            for n in range(3):
                r += (self.white[i][n])
            r += '\n'

        print(r)

    def white_clockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed
        blue = self.blue[2]
        red = self.red[2]
        green = self.green[2]
        orange = self.orange[2]

        #   Shift the values
        self.blue[2] = orange
        self.red[2] = blue
        self.green[2] = red
        self.orange[2] = green

        #   Rotate matrix
        np.rot90(self.white, 3)

    def white_counterclockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed
        blue = self.blue[2]
        red = self.red[2]
        green = self.green[2]
        orange = self.orange[2]

        #   Shift the values
        self.blue[2] = red
        self.red[2] = green
        self.green[2] = orange
        self.orange[2] = blue

        #   Rotate matrix
        np.rot90(self.white, 1)

    def orange_clockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed *note: see if faster to reshape b,w,g, take the bottom then re-reshape
        yellow = np.array(self.yellow[2]).reshape(-1, 1)
        blue = np.array(self.blue)
        white = self.green[2]
        green = self.orange[2]

        #   Shift the values
        self.yellow[2] = orange
        self.blue[2] = blue
        self.green[2] = red
        self.orange[2] = green

        #   Rotate matrix
        np.rot90(self.white, 3)

    def orange_counterclockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed
        blue = self.blue[2]
        red = self.red[2]
        green = self.green[2]
        orange = self.orange[2]

        #   Shift the values
        self.blue[2] = red
        self.red[2] = green
        self.green[2] = orange
        self.orange[2] = blue

        #   Rotate matrix
        np.rot90(self.white, 1)
