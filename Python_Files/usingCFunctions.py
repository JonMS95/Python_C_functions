# First of all, ctypes (built-in) module should be imported.

import ctypes
from usingCFunctions_constants import PATH_CHECK_SIGN, PATH_SQUARE, TEST_INTEGER_AMOUNT
from random import randint
from squareClass import Square
import time

# Now, import the symbols from the .so files. The objects that will be created do behave as Python classes.

C_checkIntSign = ctypes.CDLL(PATH_CHECK_SIGN)
C_squareNumber = ctypes.CDLL(PATH_SQUARE)

# The type of the arguments that are going to be passed to the functions within the .so files should be previously
# specified. Therefore, the Python code itself will cast it to the specified C data type.
C_checkIntSign.check.argtypes       = [ctypes.c_int]
C_squareNumber.testSquare.argtypes  = [ctypes.c_int]

# Let's create a random list of integers. While each number is generated, it's also being evaluated by the C function
# that returns the sign of the number. Hence, it's being stored as well.
numbersAndSigns = []
for i in range(10):
    x = randint(-5, 5)
    signCharacter = chr(C_checkIntSign.check(x))
    numbersAndSigns.append([x, signCharacter])

# After storing the numbers and the sign for each them, print them.
for x in numbersAndSigns:
    space = ""
    if x[1] != 'n':
        print(" ", end='')
    
    print(str(x[0]) + '\t' + x[1])

# Now, let's compare the performance for Python and C scripts:
sq = Square()

time_start = time.perf_counter_ns()
ret = sq.testSquare(TEST_INTEGER_AMOUNT)
elapsed_time_Python = time.perf_counter_ns() - time_start

time_start = time.perf_counter_ns()
ret = C_squareNumber.testSquare(TEST_INTEGER_AMOUNT)
elapsed_time_C = time.perf_counter_ns() - time_start

print('\n' + "Python time: " + '\t' + str(elapsed_time_Python))
print("C time: " + '\t' + str(elapsed_time_C))