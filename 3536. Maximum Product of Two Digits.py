def maxProduct(n: int) -> int:
    sorted_n = sorted(str(n), reverse=True)

    return int(sorted_n[0]) * int(sorted_n[1])


print(maxProduct(n = 31))