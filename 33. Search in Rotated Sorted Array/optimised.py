#!/usr/bin/env python

from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] == target:
            return l

        if nums[r] == target:
            return r

        if nums[l] <= nums[mid]:
            if nums[l] < target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
            
        else:
            if nums[mid] < target < nums[r]:
                l = mid + 1

            else:
                r = mid - 1
    
    return -1


print(search([4,5,6,7,0,1,2], 0))
