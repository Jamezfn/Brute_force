#!/usr/bin/env python

def decodeString(s: str) -> str:
    stack = []
    curr_str = ""
    curr_number = 0

    for char in s:
        if char.isdigit():
            curr_number = curr_number * 10 + int(char)
        elif char == "[":
            stack.append(curr_str)
            stack.append(curr_number)
            curr_str = ""
            curr_number = 0
        elif char == "]":
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += char


    return curr_str


print(decodeString("3[a2[c]]"))
