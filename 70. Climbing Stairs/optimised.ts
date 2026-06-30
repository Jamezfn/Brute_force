function climbStairs(n: number): number {
    const dp: number[] = new Array(n + 2).fill(0);
    dp[n] = 1;

    for (let i = n - 1; i > -1; i--) {
        dp[i] = dp[i + 1] + dp[i + 2];
    }

    return dp[0];
};

console.log(climbStairs(3));