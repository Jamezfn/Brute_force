#!/usr/bin/env python

from typing import List

def containsNearbyAlmostDuplicate(nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    """Contains Duplicate"""
    buckets = {}
    bucket_size = valueDiff + 1

    for i, num in enumerate(nums):
        bucket_id = num // bucket_size

        if bucket_id in buckets:
            return True

        if (bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff):
            return True

        if (bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff):
            return True

        buckets[bucket_id] = num

        if i >= indexDiff:
            old_bucket = nums[i - indexDiff] // bucket_size
            del buckets[old_bucket]

    return False

print(containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
print(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
