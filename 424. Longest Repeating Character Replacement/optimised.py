#!/usr/bin/env python

def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    count = {}
    res = 0
    
    l = 0
    maxf = 0
    for r in range(n):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
