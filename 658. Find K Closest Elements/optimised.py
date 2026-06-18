#!/usr/bin/env python

from typing import List

def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - k

    while l < r:
        mid = (l + r) // 2

        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid

    return arr[l: l + k]

print(findClosestElements([1,2,3,4,5], 4, 3))
