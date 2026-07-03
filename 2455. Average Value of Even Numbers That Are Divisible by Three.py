from typing import List

def averageValue(nums: List[int]) -> int:
    count = 0
    total = 0
    for num in nums:
        if num % 3 == 0 and num % 2 == 0:
            total = total + num
            count = count + 1
    if count == 0:
        return 0
    return int(total / count)



print(averageValue(nums = [1,3,6,10,12,15]))
print(averageValue(nums = [9,3,8,4,2,5,3,8,6,1]))