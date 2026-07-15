#!/usr/bin/env python

def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""

    chars = set(s)

    for i in range(len(s)):
        c = s[i]
        op = c.swapcase()

        if op not in chars:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i + 1:])

            return left if len(left) >= len(right) else right

    return s

print(longestNiceSubstring("YazaAay"))
