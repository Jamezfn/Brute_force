function climbStairs(n: number): number {
	const memo: Map<number, number> = new Map();
	function dfs(step: number): number {
		if (memo.has(step)) return memo.get(step)!;
		if (step == n) return 1;
		if (step > n) return 0;

		const k = dfs(step + 1) + dfs(step + 2);
		memo.set(step, k);

		return k;
	}

	return dfs(0);
};

console.log(climbStairs(3));
