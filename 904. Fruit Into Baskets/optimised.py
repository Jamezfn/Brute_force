#!/usr/bin/env python

from typing import List

def totalFruit(fruits: List[int]) -> int:
    n = len(fruits)
    m = {}
    ans = 0
    i = 0
    for j in range(n):
        m[fruits[j]] = m.get(fruits[j], 0) + 1
        while len(m) > 2:
            m[fruits[j]] -= 1

            if m[fruits[i]] == 0:
                del m[fruits[i]]

            i += 1
        ans = max(ans, j - i + 1)

    return ans


print(totalFruit([1,2,1]))
