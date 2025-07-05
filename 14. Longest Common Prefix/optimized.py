#!/usr/bin/env python3
from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    max_len = min(len(s) for s in strs)
    low, high = 0, max_len
    lcp_len = 0
    while low < high:
        mid = (low + high) // 2
        prefix = strs[0][:mid]
        if all(s.startswith(prefix) for s in strs):
            lcp_len = mid
            low = mid + 1
        else:
            high = mid - 1
    return strs[0][:lcp_len]

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
