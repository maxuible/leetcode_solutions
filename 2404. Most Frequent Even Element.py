from typing import List

def mostFrequentEven(nums: List[int]) -> int:
    freq = {}

    for num in nums:
        
        if num % 2 == 0:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1

    if len(freq) == 0:
        return -1

    sorted_dict = sorted(freq.items(), key=lambda item: (-item[1],item[0]))



    return sorted_dict[0][0]

# print(mostFrequentEven(nums = [4,4,4,9,2,4]))
print(mostFrequentEven(nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
