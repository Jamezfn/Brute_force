#!/usr/bin/env python


def longestValidParentheses(s: str) -> int:
    n = len(s)

    best = 0
    for i in range(n):
        balance = 0
        for j in range(i, n):
            if s[j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                break

            if balance == 0:
                best = max(best, j - i + 1)

    return best

print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))
print(longestValidParentheses(""))
