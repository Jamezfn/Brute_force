#!/usr/bin/env python

def minimumRecolors(blocks: str, k: int) -> int:
    ans = float("inf")

    for i in range(len(blocks) - k + 1):
        white = 0
        for j in range(i, i + k):
            if blocks[j] == "W":
                white += 1
        ans = min(ans, white)

    return ans


print(minimumRecolors("WBBWWBBWBW", 7))
