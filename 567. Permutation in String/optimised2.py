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

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)

    l = 0
    for r in range(n, m):
        if matches == 26: return True

        idx = ord(s2[r]) - ord('a')
        s2Count[idx] += 1
        if s1Count[idx] == s2Count[idx]:
            matches += 1
        elif s1Count[idx] + 1 == s2Count[idx]:
            matches -= 1

        idx = ord(s2[l]) - ord('a')
        s2Count[idx] -= 1
        if s1Count[idx] == s2Count[idx]:
            matches += 1
        elif s1Count[idx] + 1 == s2Count[idx]:
            matches -= 1

        l += 1

    return matches == 26


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
