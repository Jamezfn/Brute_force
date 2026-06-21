#!/usr/bin/env python

from typing import List

def findLength(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    m = len(nums2)

    ans = 0

    for i in range(n):
        for j in range(m):
            l = 0

            while i + l < n and j + l < m and nums1[i + l] == nums2[j + l]:
                l += 1

            ans = max(ans, l)

    return ans

print(findLength([1,2,3,2,1], [3,2,1,4,7]))
