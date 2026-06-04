function longestValidParentheses(s: string): number {
	const n = s.length;

	let best: number = 0;

	for (let i = 0; i < n; i++) {
		let balance = 0;
		for (let j = i; j < n; j++) {
			if (s[j] === '(') {
				balance++;
			} else {
				balance--;
			}

			if (balance < 0) break;
			if (balance === 0) {
				best = Math.max(best, j - i + 1);
			}
		}
	}

	return best;
};

console.log(longestValidParentheses("(()"));
console.log(longestValidParentheses(")()())"));
console.log(longestValidParentheses(""));
