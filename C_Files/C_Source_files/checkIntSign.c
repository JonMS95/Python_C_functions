/// @brief The function below returns '0' if the number is equal to zero, 'p' if it's positive, or 'n' if it's negative.
/// @param input The number which sign is meant to be returned. 
/// @return The sign of the number that has been passed as input parameter:
/// 'p' for positive, 'n' for negative or '0' for 0.
char check(int input)
{
    return (input == 0 ? '0' : (input > 0 ? 'p' : 'n'));
}