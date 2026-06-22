#!/usr/bin/env python

def new21Game(n: int, k: int, maxPts: int) -> float:
    memo = {}

    def dfs(score):
        if score in memo:
            return memo[score]

        if score >= k:
            return 1.0 if score <= n else 0.0

        prob = 0
        for draw in range(1, maxPts + 1):
            prob += dfs(score + draw)

        prob /= maxPts
        memo[score] = prob
        return prob
    
    return dfs(0)


print(new21Game(10, 1, 10))
