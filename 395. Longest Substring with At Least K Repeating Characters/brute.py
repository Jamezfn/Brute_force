#!/usr/bin/env python

from collections import Counter

def longestSubstring(s: str, k: int) -> int:
    """Longest Substring with At Least K Repeating Characters"""
    n = len(s)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            freq = Counter(substring)

            if all(count >= k for count in freq.values()):
                ans = max(ans, len(substring))

    return ans

print(longestSubstring("aaabb", 3))
print(longestSubstring("ababbc", 2))

print(longestSubstring("aabafbbb", 2))
