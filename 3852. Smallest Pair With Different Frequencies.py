# You are given an integer array nums.
#
# Consider all pairs of distinct values x and y from nums such that:
#
# x < y
# x and y have different frequencies in nums.
# Among all such pairs:
#
# Choose the pair with the smallest possible value of x.
# If multiple pairs have the same x, choose the one with the smallest possible value of y.
# Return an integer array [x, y]. If no valid pair exists, return [-1, -1].
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,2,3,4]
#
# Output: [1,3]
#
# Explanation:
#
# The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is [1, 3].
#
# Example 2:
#
# Input: nums = [1,5]
#
# Output: [-1,-1]
#
# Explanation:
#
# Both values have the same frequency, so no valid pair exists. Return [-1, -1].
#
# Example 3:
#
# Input: nums = [7]
#
# Output: [-1,-1]
#
# Explanation:
#
# There is only one value in the array, so no valid pair exists. Return [-1, -1].

from collections import Counter

def minDistinctFreqPair(nums: list[int]) -> list[int]:
    nums_sorted = sorted(nums)

    # print(nums_sorted)
    smallest_num = nums_sorted[0]
    smallest_num_freq = 0


    i = 0

    #outer loop to count the min
    while i < len(nums_sorted):
        if nums_sorted[i] == smallest_num:
            smallest_num_freq += 1
            i += 1
            continue
        test_target = nums_sorted[i]
        test_target_freq = 0
        #inner loop: loops until a different freq is found
        while i < len(nums_sorted):
            if nums_sorted[i] == test_target:
                test_target_freq += 1
                i += 1
                continue
            if test_target_freq != smallest_num_freq:
                return [smallest_num, test_target]
            break
        if test_target_freq != smallest_num_freq:
            return [smallest_num, test_target]
    return [-1, -1]





# print(minDistinctFreqPair([1,1,2,2,3,4]))
print(minDistinctFreqPair([5,5,4]))
