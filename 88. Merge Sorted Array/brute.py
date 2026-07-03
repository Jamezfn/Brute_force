#!/usr/bin/env python

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(n):
        nums1[m + i] = nums2[i]

    nums1.sort()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
