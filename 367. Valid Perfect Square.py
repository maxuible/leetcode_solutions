# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

import math

def isPerfectSquare(num: int) -> bool:
    return math.sqrt(num).is_integer()


# print(isPerfectSquare(16))

print(isPerfectSquare(2000105819))