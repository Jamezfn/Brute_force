#!/usr/bin/env python

def checkInclusion(s1: str, s2: str) -> bool:
    n = len(s1)
    m = len(s2)

    if n > m:
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    for i in range(n):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    if s1Count == s2Count:
        return True

    for i in range(n, m):
        s2Count[ord(s2[i]) - ord('a')] += 1
        s2Count[ord(s2[i - n]) - ord('a')] -= 1

        if s2Count == s1Count:
            return True

    return False

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
