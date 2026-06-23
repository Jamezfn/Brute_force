#!/usr/bin/env python

from typing import List

def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    ans = 0
    for i in range(n):
        basket = {}

        for j in range(i, n):
            basket[fruits[j]] = basket.get(fruits[j], 0) + 1
            if len(basket) > 2:
                break
            ans = max(ans, j - i + 1)

    return ans

print(totalFruit([1,2,1]))
