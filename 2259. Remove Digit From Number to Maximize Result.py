def removeDigit(number: str, digit: str) -> str:

    highest_int = -1

    i = 0

    while i < len(number):
        if number[i] == digit:
            # continue
            if int(number[:i] + number[i+1:]) > highest_int:
                highest_int = int(number[:i] + number[i+1:])
        i += 1



    return str(highest_int)


print(removeDigit(number = "123", digit = "3"))



# n = "max"

# print(n[:1:])