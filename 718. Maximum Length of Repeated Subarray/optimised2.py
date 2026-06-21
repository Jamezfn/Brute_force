#!/usr/bin/env python

from typing import List

def findLength(nums1: List[int], nums2: List[int]) -> int:
    m = len(nums1)
    n = len(nums2)

    if m < n:
        nums1, nums2, m, n = nums2, nums1, n, m

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    ans = 0
    for i in range(1, m + 1):
        x = nums1[i - 1]

        for j in range(1, n + 1):
            if x == nums2[j - 1]:
                val = nums2[j - 1]
                if val > ans:
                    ans = val
            else:
                curr[j] = 0

            curr, prev = prev, curr
            

    return ans

print(findLength([1,2,3,2,1], [3,2,1,4,7]))
