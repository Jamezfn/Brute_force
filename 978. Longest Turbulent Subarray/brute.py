#!/usr/bin/env python

from typing import List

def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    if n == 0:
        return 1
    ans = 1
    for i in range(n):
        l = 1
        prev = 0

        for j in range(i + 1, n):
            if arr[j - 1] < arr[j]:
                curr = 1
            elif arr[j - 1] > arr[j]:
                curr = -1
            else:
                break

            if prev == 0 or curr != prev:
                l += 1
                ans = max(ans, l)
                prev = curr
            else:
                break

    return ans

print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
