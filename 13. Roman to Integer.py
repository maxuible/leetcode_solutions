def romanToInt(s: str) -> int:
    sum = 0
    index = 0
    for i in range(len(s)):
        if index == len(s):
            break
        digit = s[index]
        if digit == 'I':
            if index < len(s) - 1 and s[index + 1] == 'V':
                sum = sum + 4
                index = index + 2
                continue
            elif index < len(s) - 1 and s[index + 1] == 'X':
                sum = sum + 9
                index = index + 2
                continue
            else:
                sum = sum + 1
        elif digit == 'X':
            if index < len(s) - 1 and s[index + 1] == 'L':
                sum = sum + 40
                index = index + 2
                continue
            elif index < len(s) - 1 and s[index + 1] == 'C':
                sum = sum + 90
                index = index + 2
                continue
            else:
                sum = sum + 10
        elif digit == 'C':
            if index < len(s) - 1 and s[index + 1] == 'D':
                sum = sum + 400
                index = index + 2
                continue
            elif index < len(s) - 1 and s[index + 1] == 'M':
                sum = sum + 900
                index = index + 2
                continue
            else:
                sum = sum + 100
        else:
            if digit == 'V':
                sum = sum + 5
            elif digit == 'L':
                sum = sum + 50
            elif digit == 'D':
                sum = sum + 500
            elif digit == 'M':
                sum = sum + 1000
        index = index + 1
        continue
    return sum



print(romanToInt(s = "MCMXCIV"))