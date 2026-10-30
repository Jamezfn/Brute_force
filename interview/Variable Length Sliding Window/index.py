#!/usr/bin/env python

def fruit_into_baskets(fruits):
    max_fruits = 0
    state = {}
    start = 0

    for end in range(len(fruits)):
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1

            if state[fruits[start]] == 0:
                del state[fruits[start]]

            start += 1

        max_fruits =max(max_fruits, end - start + 1)

    return max_fruits

print(fruit_into_baskets([3, 3, 2, 1, 2, 1, 0]))
