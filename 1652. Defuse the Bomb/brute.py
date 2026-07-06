#!/usr/bin/env python

from typing import List

def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    res = [0] * n
    for i in range(n):
        if k > 0:
            for j in range(i + 1, i + abs(k) + 1):
                res[i] += code[j % n]
        elif k < 0:
            for j in range(i - 1, i - abs(k) - 1, -1):
                res[i] += code[(j % n)]

    return res

print(decrypt([5,7,1,4], 3))
print(decrypt([5,7,1,4], 0))
print(decrypt([2,4,9,3], -2))
