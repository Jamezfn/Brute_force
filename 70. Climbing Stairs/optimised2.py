#!/usr/bin/env python
def climbStairs(n: int) -> int:
	if n <= 2:
		return n
	
	a = 1
	b = 1

	for _ in range(n - 1):
		a, b = b, a + b
	return b

print(climbStairs(3))