def strStr(haystack: str, needle: str) -> int:

    if not needle in haystack:
        return -1
    else:
        return haystack.index(needle)