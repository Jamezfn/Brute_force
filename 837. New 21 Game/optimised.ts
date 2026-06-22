function new21Game(n: number, k: number, maxPts: number): number {
	if (k == 0 || n >= k + maxPts) {
		return 1.0;
	}

	const dp = new Array(k + maxPts).fill(0);

	for (let i = k; i < n + 1; i++) {
		dp[i] = 1;
	}

	let wSum = 0;

	for (let i = k; i < k + maxPts; i++) {
		wSum += dp[i];
	}

	for (let i = k - 1; i > -1; i--) {
		dp[i] = wSum / maxPts;
		wSum += dp[i] - dp[i + maxPts];
	}

	return dp[0];
};

console.log(new21Game(10, 1, 10));
