function longest_valid_parentheses(s: string): number {
	const stack: number[] = [-1];
	let maxLen: number = 0;

	for (let i = 0; i < s.length; i++) {
		let c: string = s[i];

		if (c === "(") {
			stack.push(i);
		} else {
			stack.pop();

			if (stack.length === 0) {
				stack.push(i);
			} else {
				maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
			}
		}
	}

	return maxLen;
}

console.log(longest_valid_parentheses("((()()())"));