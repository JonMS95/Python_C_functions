#include <stdlib.h>
#include <time.h>

/// @brief Returns the square number of the integer passed as input variable.
int square(int input)
{
    return (input * input);
}

/// @brief Performs a test. It's going to be used against a similar Python function.
/// @param integerAmount The amount of numbers (starting from 1) which squares have to be calculated and then added.
/// @return The sum of all the previously calculated square numbers.
int testSquare(int integerAmount)
{
    int i, ret = 0;

    for (i = 1; i < integerAmount + 1; i++)
    {
        ret += square(i);
    }

    return ret;
}