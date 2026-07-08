def maxLengthBetweenEqualCharacters(s: str) -> int:
    largest_sub_string = -1
    i = 0
    while i < len(s):
        if s[i] in s[i+1:]:
            if largest_sub_string < s[i+1:].rindex(s[i]):
                largest_sub_string = s[i+1:].rindex(s[i])
        i = i + 1

    return largest_sub_string


# print(maxLengthBetweenEqualCharacters("aa"))
print(maxLengthBetweenEqualCharacters("abca"))