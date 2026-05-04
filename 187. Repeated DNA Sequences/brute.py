#!/usr/bin/env python

def findRepeatedDnaSequences(s: str):
    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        sub = s[i:i+10]
        if sub in seen:
            repeated.add(sub)
        else:
            seen.add(sub)
    return list(repeated)

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))

s = "AAAAAAAAAAAAA"  # 13 A's
print(findRepeatedDnaSequences(s))
