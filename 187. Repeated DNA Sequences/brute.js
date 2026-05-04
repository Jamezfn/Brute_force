var findRepeatedDnaSequences = function(s) {
	const seen = new Set();
	const repeated = new Set();

	for (let i = 0; i <= s.length; i++) {
		const sub = s.slice(i, i + 10);

		if (seen.has(sub)) {
			repeated.add(sub);
		} else {
			seen.add(sub);
		}
	}

	return [...repeated];
};

console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
console.log(findRepeatedDnaSequences("AAAAAAAAAAAAA"));
