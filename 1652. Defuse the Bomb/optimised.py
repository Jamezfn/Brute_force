#!/usr/bin/env python

from typing import List

def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0] * n
    sm = 0
    l = 0
    for r in range(n + abs(k)):
        sm += code[r % n]

        if r - l + 1 > abs(k):
            sm -= code[l % n]
            l = (l + 1) % n

        if r - l + 1 == abs(k):
            if k > 0:
                res[(l - 1)] = sm
            elif k < 0:
                res[(r + 1) % n] = sm


    return res

print(decrypt([5,7,1,4], 3))
print(decrypt([5,7,1,4], 0))
print(decrypt([2,4,9,3], -2))
