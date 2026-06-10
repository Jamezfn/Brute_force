#!/usr/bin/env python

from collections import Counter
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    n = len(s)
    len_p = len(p)
    an_p = Counter(p) 
    
    res = []
    for i in range(0, n, len_p):
        an_str = s[i:i+len_p]
        an = Counter(an_str)

        if an == an_p:
            res.append(i)

    return res

print(findAnagrams("cbaebabacd", "abc"))
