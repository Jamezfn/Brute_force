#!/usr/bin/env python

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)
    s1Count = [0] * 26
    for i in range(n):
        s1Count[ord(s1[i]) - ord('a')] += 1

    for i in range(n, m):
        window = s2[i - n:i]

        s2Count = [0] * 26
        for j in range(len(window)):
            s2Count[ord(window[j]) - ord('a')] += 1
        if s1Count == s2Count:
            return True

    return False

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
