def subtractProductAndSum(n: int) -> int:
    product = 1
    sum = 0
    for digit in str(n):
        product = product * int(digit)
        sum = sum + int(digit)
    return product - sum

print(subtractProductAndSum(n = 234))