function longestNiceSubstring(s: string): string {
	if (s.length < 2) return "";
	
	const chars = new Set(s);

	for (let i = 0; i < s.length; i++) {
		const c = s[i]
		const op = c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase(); 

		if (!chars.has(op)) {
			const left = longestNiceSubstring(s.substring(0, i));
			const right = longestNiceSubstring(s.substring(i + 1));

			return left.length >= right.length ? left : right;
		}
	}

	return s
}

console.log(longestNiceSubstring("YazaAay"));
