def isSameAfterReversals(num: int) -> bool:

    if int(str(int(str(num)[::-1]))[::-1]) == num:
        return True

    return False


print(isSameAfterReversals(num = 526))