#!/usr/bin/env python


def nextGreaterElement(nums):
    n = len(nums)
    stack = []

    result = [-1] * n
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result

print(nextGreaterElement([102, 101, 103, 102, 104, 103]))
