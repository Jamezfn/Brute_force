#!/usr/bin/env python

def characterReplacement(s: str, k: int) -> int:
    max_length = 0
    state = {}
    max_freq = 0
    start = 0

    for end in range(len(s)):
        state[s[end]] = state.get(s[end], 0) + 1
        max_freq = max(max_freq, state[s[end]])

        if k + max_freq < end - start + 1:
            state[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

print(characterReplacement("BBABCCDD", 2))
