#!/usr/bin/env python

def longestValidParentheses(s: str) -> int:
    n = len(s)
    stack = [-1]
    max_len = 0
    for i in range(n):
        if s[i]  == '(':
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                l = i - stack[-1]
                max_len = max(max_len, l)

    return max_len

print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))
print(longestValidParentheses(""))
