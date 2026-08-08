def hasSpecialSubstring(s: str, k: int) -> bool:

    i = 0
    while i < len(s):

        if s[i:i+k] == s[i] * k:
            if i == 0 or s[i-1] != s[i]:
                if i == len(s) - k or (i+k < len(s) and s[i+k] != s[i]):
                    return True

        i = i + 1


    return False


print(hasSpecialSubstring(s = "aaabaaa", k = 3))
print(hasSpecialSubstring(s = "dii", k = 1))
print(hasSpecialSubstring(s = "ccc", k = 2))
print(hasSpecialSubstring(s = "bfggb", k = 2))