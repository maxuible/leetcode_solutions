# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
#
#
#
# Example 1:
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Explanation:
#
# The strings s and t can be made identical by:
#
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:
#
# Input: s = "f11", t = "b23"
#
# Output: false
#
# Explanation:
#
# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.
#
# Example 3:
#
# Input: s = "paper", t = "title"
#
# Output: true

import numpy as np

def isIsomorphic(s: str, t: str) -> bool:



    while len(s) > 0 and len(t) > 0:

        letter_s = s[0]
        letter_t = t[0]

        if s.count(letter_s) == t.count(letter_t):

            indices_s = [i for i, x in enumerate(s) if x == letter_s]
            indices_t = [i for i, x in enumerate(t) if x == letter_t]

            if indices_t == indices_s:
                s = s.replace(letter_s, "")
                t = t.replace(letter_t, "")
            else:
                return False
        else:
            return False

    if len(s) == 0 and len(t) == 0:
        return True
    else:
        return False


# print(isIsomorphic("egg", "add"))

print(isIsomorphic("bbbaaaba", "aaabbbba"))


