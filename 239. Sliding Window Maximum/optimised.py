#!/usr/bin/env python

from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    result = []
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
