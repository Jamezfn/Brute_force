#!/usr/bin/env python

def longestNiceSubstring(s: str) -> str:
    n = len(s)
    ans = ""

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j + 1]
            chars = set(sub)

            nice = True
            for c in chars:
                if c.swapcase() not in chars:
                    nice = False
            
            if nice and len(sub) > len(ans):
                ans = sub

    return ans

print(longestNiceSubstring("YazaAay"))
