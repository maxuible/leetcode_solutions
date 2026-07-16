from typing import List
def plusOne(digits: List[int]) -> List[int]:

    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
                break
            continue
        else:
            digits[i] += 1
            break

    return digits

# print(plusOne([1,2,3]))
print(plusOne([9,9,9]))