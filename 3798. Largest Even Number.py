def largestEven(s: str) -> str:

    i = len(s) - 1

    while i > -1:
        if s[i] == '2':
            return s[0:i+1]
        i = i - 1

    return ""
