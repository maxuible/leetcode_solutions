from typing import List

def getMinDistance(nums: List[int], target: int, start: int) -> int:

    lowest = abs(nums.index(target) - start)

    i = 0

    while i < len(nums):
        if nums[i] == target:
            if abs(i - start) < lowest:
                lowest = abs(i - start)
        i += 1


    return lowest


# print(getMinDistance(nums = [1,2,3,4,5], target = 5, start = 3))
print(getMinDistance(nums = [5,7,7,5], target = 5, start = 2))