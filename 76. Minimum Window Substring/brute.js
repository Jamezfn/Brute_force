var minWindow = function(s, t) {
	const m = s.length;
	let minWindow = "";

	const countChar = (str, ch) => [...str].filter((c) => c === ch);

	for (let i = 0; i < m; i++) {
		for (j = i + 1; j <= m; j++) {
			const substring = s.slice(i, j);

			const valid = [...new Set(t)].every(
				(c) => countChar(substring, c) >= countChar(t, c)
			);

			if (valid && (minWindow === "" || substring.length < minWindow.length)) {
				minWindow = substring;
			}
		}
	}

	return minWindow;
};

console.log(minWindow("ADOBECODEBANC", "ABC"));
console.log(minWindow("a", "a"));
console.log(minWindow("a", "aa"));
