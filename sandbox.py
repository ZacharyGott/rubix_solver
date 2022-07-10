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
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y']
     ]

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

start = time.time()  # Start timer

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

##
for i in range(3):
    test.blue_counterclockwise()
    test.white_clockwise()
    test.orange_counterclockwise()


##

end = time.time()  # End timer

test.print_cube()
print(end - start)

# print(np.array(test.yellow).reshape(1, -1))
