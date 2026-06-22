#!/usr/bin/env python

def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0

    dp = [0] * (k + maxPts)

    for i in range(k, n + 1):
        dp[i] = 1

    windowSum = 0

    for i in range(k, k + maxPts):
        windowSum += dp[i]

    for i in range(k - 1, -1, -1):
        dp[i] = windowSum / maxPts
        windowSum += dp[i] - dp[i + maxPts]

    return dp[0]

print(new21Game(10, 1, 10))
