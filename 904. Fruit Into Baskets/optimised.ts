function totalFruit(fruits: number[]): number {
	const n = fruits.length;
	const m: Map<number, number> = new Map();
	let ans = 0;
	let i = 0;
	for (let j = i; j < n; j++) {
		m.set(fruits[j], (m.get(fruits[j]) ?? 0) + 1);
		while (m.size > 2) {
			m.set(fruits[j], (m.get(fruits[j]) ?? 0) - 1);
			if (m.get(fruits[j]) === 0) {
				m.delete(fruits[i]);
			}
			l++;
		}
		ans = Math.max(ans, j - i + 1);
	}

	return ans;
};

console.log(totalFruit([1,2,1]));
