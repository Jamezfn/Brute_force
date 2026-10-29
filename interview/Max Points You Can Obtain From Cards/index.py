#!/usr/bin/env python

from typing import List

def maxScore(cards: List[int], k: int) -> int:
    total = sum(cards)
    if k == total:
        return total

    state = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        state += cards[end]
        if end - start + 1 == len(cards) - k:
            max_points = max(total - state, max_points)
            state -= cards[start]
            start += 1


    return max_points

print(maxScore([2,11,4,5,3,9,2], 3))
