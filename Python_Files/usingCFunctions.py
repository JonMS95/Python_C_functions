# First of all, ctypes (built-in) module should be imported.

import ctypes
from usingCFunctions_constants import PATH_CHECK_SIGN, PATH_SQUARE

# Now, import the symbols from the .so files. The objects that will be created do behave as Python classes.

C_checkIntSign = ctypes.CDLL(PATH_CHECK_SIGN)
C_squareNumber = ctypes.CDLL(PATH_SQUARE)