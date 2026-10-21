#!/usr/bin/env python

def max_area(heights):
    left, right = 0, len(heights) - 1

    current_max = 0

    while left < right:
        width = right - left

        height = min(heights[left], heights[right])
        current_area = width * height

        current_max = max(current_area, current_max)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return current_max


print(max_area([3, 4, 1, 2, 2, 4, 1, 3, 2]))
