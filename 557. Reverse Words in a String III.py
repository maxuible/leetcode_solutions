# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



def reverseWords(s: str) -> str:

    ret_list = []

    list_of_words = s.split()

    for word in list_of_words:
        
        ret_list.append(word[::-1])

    print(ret_list)

    return " ".join(ret_list)

print(reverseWords(s = "Let's take LeetCode contest"))