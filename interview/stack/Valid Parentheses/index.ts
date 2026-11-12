
function isValid(s: string): boolean {
	const stack: string[] = [];
	const mapped: Record<string, string> = {")": "(", "}": "{", "]": "["};

	for (const char of s) {
		if (char in mapped) {
			if (stack.length === 0 || stack[stack.length - 1] !== mapped[char]) {
				return false;
			}

			stack.pop();
		} else {
			stack.push(char);
		}
	}

	return stack.length === 0;
}


console.log(isValid("(){({})}"));