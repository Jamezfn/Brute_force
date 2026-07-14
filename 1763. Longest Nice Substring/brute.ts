function isNice(sub: string): boolean {
	const chars = new Set(sub);

	for (const c of chars) {
		const ops = c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase();

		if (!chars.has(ops)) {
			return false;
		}
	}

	return true;
}

function longestNiceSubstring(s: string): string {
	let result = "";

	for (let i = 0; i < s.length; i++) {
		for (let j = i + 1; j < s.length; j++) {
			const sub = s.substring(i, j);
			if (isNice(sub) && sub.length > result.length) {
				result = sub;
			}
		}
	}

	return result;
};


console.log(longestNiceSubstring("YazaAay"));
