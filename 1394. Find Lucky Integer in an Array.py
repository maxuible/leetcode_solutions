# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
 

# Constraints:

# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500

from typing import List

def findLucky(arr: List[int]) -> int:
    sorted_arr = sorted(arr, reverse=True)
    value = sorted_arr[0]
    count = 1
    for i in range(1,len(sorted_arr)):
        if sorted_arr[i] == value:
            count += 1
        else:
            if count == value:
                return value
            value = sorted_arr[i]
            count = 1
    
    if count == value:
        return value

    return -1

print(findLucky([2,2,3,4]))