def lengthOfLastWord(s: str) -> int:

    words = s.lstrip().rstrip().split(" ")


    return len(words[-1].lstrip().rstrip())


print(lengthOfLastWord("   fly me   to   the moon  "))