def hammingWeight(n: int) -> int:
    count = 0
    for digit in str(bin(n))[2:]:
        if digit == '1':
            count += 1
    

    return count


print(hammingWeight(11))