from typing import List

def maxOperations(nums: List[int]) -> int:
    count = 0
    if len(nums) < 2:
        return count
    
    target = nums[0] + nums[1]

    while len(nums) >= 2:
        if target == nums[0] + nums[1]:
            count += 1
            nums = nums[2:]
        else:
            break

    return count


# print(maxOperations([3,2,1,4,5]))
print(maxOperations([5,3]))