# ou are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.

from typing import List

def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:

    cant_fill = 0
    for i in range(len(fruits)):
        filled = False
        for j in range(len(baskets)):
            if fruits[i] <= baskets[j]:
                filled = True
                del baskets[j]
                break;
        if not filled:
            cant_fill += 1


    return cant_fill

print(numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))