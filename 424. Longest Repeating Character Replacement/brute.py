#!/usr/bin/env python

def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    ans = 0

    for i in range(n):
        freq = [0] * 26
        max_freq = 0;

        for j in range(i, n):
            idx = ord(s[j]) - ord('A')
            freq[idx] += 1

            max_freq = max(max_freq, freq[idx])
            length = j - i + 1
            change_needed = length - max_freq

            if change_needed <= k:
                ans = max(ans, length)

    return ans


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
