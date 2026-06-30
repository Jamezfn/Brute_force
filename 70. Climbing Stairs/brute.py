#!/usr/bin/env python

def climbStairs(n: int) -> int:
    memo = {}
    def dfs(step):
        if step in memo:
            return memo[step]
        
        if step == n:
            return 1
        
        if step > n:
            return 0
        
        k = dfs(step + 1) + dfs(step + 2)
        memo[step] = k

        return k

    return dfs(0)

print(climbStairs(3))
