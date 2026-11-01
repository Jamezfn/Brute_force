function characterReplacement(s: string, k: number): number {
	let maxLength: number = 0;
	let maxFreq: number = 0
	const state: Map<string, number> = new Map();
	let start: number = 0;

	for (let end = 0; end < s.length; end++) {
		state.set(s[end], (state.get(s[end]) ?? 0) + 1);
		maxFreq = Math.max(maxFreq, state.get(s[end]) ?? 0);

		if (maxFreq + k < end - start + 1) {
			state.set(s[start], state.get(s[start])! - 1);
			start++;
		}

		maxLength = Math.max(maxLength, end - start + 1);
	}

	return maxLength;
}

console.log(characterReplacement("BBABCCDD", 2));