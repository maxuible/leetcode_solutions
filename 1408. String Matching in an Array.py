# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.

from typing import List

def stringMatching(words: List[str]) -> List[str]:

    ret_list = []

    for word_a in words:
        for word_b in words:
            if word_a == word_b:
                continue
            elif word_a in word_b:
                ret_list.append(word_a)

    return list(set(ret_list))

print(stringMatching(["mass","as","hero","superhero"]))