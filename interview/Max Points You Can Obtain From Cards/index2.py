#!/usr/bin/env python

from typing import List

def maxScore(cards: List[int], k: int) -> int:
    n = len(cards)
    max_score = 0

    for i in range(k + 1):
        left_sum = sum(cards[:i])
        right_sum = sum(cards[n - (k - i):]) if k - 1 > 0 else 0

        score = left_sum + right_sum
        max_score = max(max_score, score)

    return max_score

print(maxScore([2,11,4,5,3,9,2], 3))
