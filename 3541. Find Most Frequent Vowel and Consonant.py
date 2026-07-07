

def maxFreqSum(s: str) -> int:
    vowel_freq = 0
    const_freq = 0

    sorted_word = sorted(s)
    
    curr_let = sorted_word[0]
    curr_count = 1
    for i in range(1, len(sorted_word)):
        if sorted_word[i] != curr_let:
            if curr_let in ['a', 'e', 'i', 'o', 'u'] and curr_count > vowel_freq:
                vowel_freq = curr_count
            elif not curr_let in ['a', 'e', 'i', 'o', 'u'] and curr_count > const_freq:
                const_freq = curr_count
            curr_count = 1
            curr_let = sorted_word[i]
            continue
        elif sorted_word[i] == curr_let:
            curr_count += 1
            
    if curr_let in ['a', 'e', 'i', 'o', 'u'] and curr_count > vowel_freq:
        vowel_freq = curr_count
    elif not curr_let in ['a', 'e', 'i', 'o', 'u'] and curr_count > const_freq:
        const_freq = curr_count
        

    return vowel_freq + const_freq



# print(maxFreqSum(s = "successes"))
print(maxFreqSum(s = "aeiaeia"))