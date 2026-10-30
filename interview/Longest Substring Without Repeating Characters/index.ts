function longestSubstringWithoutRepeat(s: string): number {
	let max_length: number = 0;
	const state: Map<string, number> = new Map();
	let start: number = 0;

	for (let end = 0; end < s.length; end++) {
		state.set(s[end], (state.get(s[end]) ?? 0) + 1);
		
		while (state.get(s[end])! > 1) {
			state.set(s[start], state.get(s[start])! - 1);
			if (state.get(s[start]) === 0) {
				state.delete(s[start]);
			}

			start++;
		}

		max_length = Math.max(max_length, end - start + 1);
	}

	return max_length;
}


console.log(longestSubstringWithoutRepeat("eghghhgg"))