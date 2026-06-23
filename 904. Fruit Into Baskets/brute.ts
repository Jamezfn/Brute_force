function totalFruit(fruits: number[]): number {
	const n = fruits.length;

	let ans = 0;
	for (let i = 0; i < n; i++) {
		const m: Map<number, number> = new Map();

		for (let j = i; j < n; j++) {
			m.set(fruits[j], (m.get(fruits[j]) ?? 0) + 1);
			if (m.size > 2) {
				break;
			}

			ans = Math.max(ans, j - i + 1);
		}
	}

	return ans;
};

console.log(totalFruit([1,2,1]));
