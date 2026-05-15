#!/usr/bin/env python

from collections import Counter

def longestSubstring(s: str, k: int) -> int:
    if len(s) < k:
        return 0

    freq = Counter(s)

    if all(feq[c] >= k for c in freq):
        return len(s)

    result = 0
    start = 0

    for i, c in enumarate(s):
        if freq[c] < k:
            result = max(result, longestSubstring(s[start:i], k))
            start = i + 1

    result = max(result, longestSubstring(s[start:], k))

    return result
