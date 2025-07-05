#!/usr/bin/env python3
from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    """Compute the longest prefix using brute force"""
    max_len = min(len(s) for s in strs)
    longest = ""
    for length in range(1, max_len+1):
        prefix = strs[0][:length]
        mismatch = False
        for s in strs:
            if not s.startswith(prefix):
                mismatch = True
                break
        if mismatch:
            return longest
        longest = prefix
    return longest

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
