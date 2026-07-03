#!/usr/bin/env python

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    l = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[l] = nums1[i]
            i -= 1
        else:
            nums1[l] = nums2[j]
            j -= 1

        l -= 1

    while j >= 0:
        nums1[l] = nums2[j]
        j -= 1
        l -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
