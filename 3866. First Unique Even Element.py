

def firstUniqueEven(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            if nums[i] not in nums[0:i] + nums[i+1:]:
                return nums[i]
        i += 1

    return -1



print(firstUniqueEven([3,4,2,5,4,6]))
print(firstUniqueEven([4,4]))