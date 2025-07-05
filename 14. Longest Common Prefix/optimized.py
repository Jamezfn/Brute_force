#!/usr/bin/env python3
from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    max_len = min(len(s) for s in strs)
    low, high = 0, max_len
    while low < high:
        mid = (low + high + 1) // 2
        prefix = strs[0][:mid]
        if all(s.startswith(prefix) for s in strs):
            low = mid
        else:
            high = mid - 1
    return strs[0][:high]

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
