def greatestLetter(s: str) -> str:
    for letter in range(90,64,-1):
        # print(letter)
        if chr(letter) in s and chr(letter + 32) in s:
            return chr(letter)
    return ""

print(greatestLetter(s = "lEeTcOdE"))