from cube import Cube
import time
import numpy as np

Wh = [
        ['1', '2', '3'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
     ]

Or = [
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o']
     ]

Bl = [
        ['1', 'b', 'b'],
        ['2', 'b', 'b'],
        ['3', 'b', 'b']
     ]

Re = [
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r']
     ]

Gr = [
        ['g', 'g', '1'],
        ['g', 'g', '2'],
        ['g', 'g', '3']
     ]

Ye = [
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['1', '2', '3']
     ]

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

start = time.time()  # Start timer

test = Cube(Wh, Or, Bl, Re, Gr, Ye)
test.orange_clockwise()

end = time.time()  # End timer

test.print_cube()
print(end - start)

# print(np.array(test.yellow).reshape(1, -1))
