from squareClass_constants import *

class Square:
    def __init__(self):
        self.string = STR_SQUARE_INIT

    def __str__(self):
        print(STR_SQUARE_STR)

    def square(self, input):
        return (input * input)

    def testSquare(self, integerAmount):
        ret = 0

        for i in range(1, integerAmount + 1):
            ret += self.square(i)
    
        return ret