from cube import Cube
import time
import numpy as np

Wh = [
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
     ]

Or = [
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
     ]

Bl = [
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']
     ]

Re = [
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']
     ]

Gr = [
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']
     ]

Ye = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
     ]

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

start = time.time()  # Start timer

test = Cube(Wh, Or, Bl, Re, Gr, Ye)
# test.white_counterclockwise()
#
# end = time.time()  # End timer
#
# test.print_cube()
# print(end - start)

print(np.array(test.yellow).reshape(1, -1))