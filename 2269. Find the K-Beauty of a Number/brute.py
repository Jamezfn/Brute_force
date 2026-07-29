#!/usr/bin/env python

def divisorSubstrings(num: int, k: int) -> int:
    ans = 0
    s = str(num)
    n = len(s)

    for i in range(n - k + 1):
        sub = int(s[i:i + k - 1])

        if sub != 0 and num % sub == 0:
            ans += 1

    return ans


print(divisorSubstrings(240, 2))
