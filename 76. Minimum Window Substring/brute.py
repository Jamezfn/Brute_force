#!/usr/bin/env python

def minWindow(s: str, t: str) -> str:
    """Minimum Window Substring"""
    if not s or not t:
        return ""

    m = len(s)
    min_window = ""

    for i in range(m):
        for j in range(i + 1, m + 1):
            substring = s[i:j]


            if all(substring.count(c) >= t.count(c) for c in t):
                if min_window == "" or len(substring) < len(min_window):
                    min_window = substring

    return min_window


print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
