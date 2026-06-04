function longestValidParentheses(s: string): number {
	const n = s.length;

	const slack: number[] = [-1];
	let max_len = 0;
	for (let i = 0; i < n; i++) {
		if (s[i] === '(') {
			slack.push(i);
		} else {
			slack.pop();

			if (slack.length === 0) {
				slack.push(i);
			} else {
				max_len = Math.max(max_len, i - slack[slack.length - 1]);
			}
		}
	}

	return max_len;
};

console.log(longestValidParentheses("(()"));
console.log(longestValidParentheses(")()())"));
console.log(longestValidParentheses(""));
