from cube import Cube
import time
import numpy as np

Wh = [
        ['1', '2', '3'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w']
     ]

Or = [
        ['o', 'o', '1'],
        ['o', 'o', '2'],
        ['o', 'o', '3']
     ]

Bl = [
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b']
     ]

Re = [
        ['1', 'r', 'r'],
        ['2', 'r', 'r'],
        ['3', 'r', 'r']
     ]

Gr = [
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g']
     ]

Ye = [
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['1', '2', '3']
     ]

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

start = time.time()  # Start timer

test = Cube(Wh, Or, Bl, Re, Gr, Ye)

##
for i in range(5):
    test.blue_clockwise()


##

end = time.time()  # End timer

test.print_cube()
print(end - start)

# print(np.array(test.yellow).reshape(1, -1))
