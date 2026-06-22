function new21Game(n: number, k: number, maxPts: number): number {
	const memo: Map<number, number> = new Map();

	function dfs(score) {
		if (memo.has(score)) return memo.get(score);

		if (score >= k) {
			if (score <= n) {
				return 1.0;
			} else {
				return 0.0;
			}
		}

		let prob = 0;
		for (let i = 1; i <= maxPts; i++) {
			prob += dfs(score + i);
		}

		prob /= maxPts;
		memo.set(score, prob);

		return prob;
	}

	return dfs(0);
};

console.log(new21Game(10, 1, 10));
