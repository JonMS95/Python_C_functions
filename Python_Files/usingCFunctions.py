# First of all, ctypes (built-in) module should be imported.

import ctypes
from usingCFunctions_constants import PATH_CHECK_SIGN, PATH_SQUARE

# Now, import the symbols from the .so files. The objects that will be created do behave as Python classes.

C_checkIntSign = ctypes.CDLL(PATH_CHECK_SIGN)
C_squareNumber = ctypes.CDLL(PATH_SQUARE)

# The type of the arguments that are going to be passed to the functions within the .so files should be previously
# specified. Therefore, the Python code itself will cast it to the specified C data type.
C_checkIntSign.function.argtypes = [ctypes.c_int]
C_squareNumber.function.argtypes = [ctypes.c_int]

print(C_checkIntSign.function(-4))
print(C_checkIntSign.function(5))
print(C_checkIntSign.function(0))