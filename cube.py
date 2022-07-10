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
        blue = np.array(self.blue[2])
        red = np.array(self.red[2])
        green = np.array(self.green[2])
        orange = np.array(self.orange[2])

        #   Shift the values
        self.blue[2] = orange
        self.red[2] = blue
        self.green[2] = red
        self.orange[2] = green

        #   Rotate matrix
        self.white = np.rot90(self.white, 3)

    # This function may be wrong
    def white_counterclockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed
        blue = np.array(self.blue[2])
        red = np.array(self.red[2])
        green = np.array(self.green[2])
        orange = np.array(self.orange[2])

        #   Shift the values
        self.blue[2] = red
        self.red[2] = green
        self.green[2] = orange
        self.orange[2] = blue

        #   Rotate matrix
        self.white = np.rot90(self.white, 1)

    def orange_clockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed *note: see if faster to reshape b,w,g, take the bottom then re-reshape
        yellow = np.array(np.rot90(self.yellow, 1)[2])
        blue = np.array(np.rot90(self.blue, 1)[2])
        white = np.array(np.rot90(self.white, 1)[2])
        green = np.array(np.rot90(self.green, 1)[0])

        #   Shift the values
        self.yellow = np.rot90(self.yellow, 1)
        self.yellow[2] = green[::-1]
        self.yellow = np.rot90(self.yellow, 3)

        #   might make function for this
        self.blue = np.rot90(self.blue, 1)
        self.blue[2] = yellow
        self.blue = np.rot90(self.blue, 3)

        self.white = np.rot90(self.white, 1)
        self.white[2] = blue
        self.white = np.rot90(self.white, 3)

        #   very cheap fix by making white a np.array, fix later
        self.green = np.rot90(self.green, 1)
        self.green[0] = white[::-1]
        self.green = np.rot90(self.green, 3)

        #   Rotate matrix
        self.orange = np.rot90(self.orange, 3)

    def orange_counterclockwise(self):
        # there may be a better way to iterate through these. Maybe having list [0, 1, 2, 3] or whatever the cube
        # index for the faces are, then looping through it in a direction dictated by clockwise or counter clockwise

        #   Saves copies of the values needed *note: see if faster to reshape b,w,g, take the bottom then re-reshape
        yellow = np.array(np.rot90(self.yellow, 1)[2])
        blue = np.array(np.rot90(self.blue, 1)[2])
        white = np.array(np.rot90(self.white, 1)[2])
        green = np.array(np.rot90(self.green, 1)[0])

        #   Shift the values
        self.yellow = np.rot90(self.yellow, 1)
        self.yellow[2] = blue
        self.yellow = np.rot90(self.yellow, 3)

        #   might make function for this
        self.blue = np.rot90(self.blue, 1)
        self.blue[2] = white
        self.blue = np.rot90(self.blue, 3)

        self.white = np.rot90(self.white, 1)
        self.white[2] = green[::-1]
        self.white = np.rot90(self.white, 3)

        #   very cheap fix by making white a np.array, fix later
        self.green = np.rot90(self.green, 1)
        self.green[0] = yellow[::-1]
        self.green = np.rot90(self.green, 3)

        #   Rotate matrix
        self.orange = np.rot90(self.orange, 1)

    def blue_clockwise(self):
        yellow = np.array(self.yellow[2])
        red = np.array(np.rot90(self.red, 1)[2])
        white = np.array(self.white[0])
        orange = np.array(np.rot90(self.orange, 1)[0])

        self.white[0] = red[::-1]

        self.orange = np.rot90(self.orange, 1)
        self.orange[0] = white
        self.orange = np.rot90(self.orange, 3)

        self.yellow[2] = orange[::-1]

        self.red = np.rot90(self.red, 1)
        self.red[2] = yellow
        self.red = np.rot90(self.red, 3)

        self.blue = np.rot90(self.blue, 3)

    def blue_counterclockwise(self):
        yellow = np.array(self.yellow[2])
        red = np.array(np.rot90(self.red, 1)[2])
        white = np.array(self.white[0])
        orange = np.array(np.rot90(self.orange, 1)[0])

        self.white[0] = orange

        self.orange = np.rot90(self.orange, 3)
        self.orange[2] = yellow
        self.orange = np.rot90(self.orange, 1)

        self.yellow[2] = red

        self.red = np.rot90(self.red, 1)
        self.red[2] = white[::-1]
        self.red = np.rot90(self.red, 3)

        self.blue = np.rot90(self.blue, 1)

