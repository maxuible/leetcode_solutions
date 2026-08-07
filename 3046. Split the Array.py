
from typing import List

def isPossibleToSplit(nums: List[int]) -> bool:

    setA = []
    setB = []

    for num in nums:
        if num not in setA:
            setA.append(num)
        elif num not in setB:
            setB.append(num)
        else:
            return False

    return True



print(isPossibleToSplit(nums = [1,1,2,2,3,4]))