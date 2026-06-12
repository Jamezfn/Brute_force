function findLHS(nums: number[]): number {
	const n = nums.length;
	let ans = 0;
	function dfs(i, seq) {
		if (seq.length && Math.max(...seq) - Math.min(...seq) === 1) {
			ans = Math.max(ans, seq.length)
		}
		if (i === n) return;

		seq.push(nums[i]);
		dfs(i + 1, seq);

		seq.pop();
		dfs(i + 1, seq);
	}

	dfs(0, []);

	return ans
};

console.log(findLHS([1, 2, 5, 6, 6]));
