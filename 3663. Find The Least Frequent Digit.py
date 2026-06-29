def getLeastFrequentDigit(n: int) -> int:
    s = str(abs(n))
    counts = {int(d): s.count(d) for d in set(s)}
    
    return min(counts, key=lambda k: (counts[k], k))



print(getLeastFrequentDigit(n = 1553322))