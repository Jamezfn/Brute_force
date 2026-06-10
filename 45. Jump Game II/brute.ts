function jump(nums: number[]): number {
	const n = nums.length;

	function dfs(i) {
		if (i >= n - 1) {
			return 0;
		}
	
		let jumps: number = Infinity;

		for (let j = 1; j <= nums[i]; j++) {
			jumps = Math.min(jumps, 1 + dfs(i + j));
		}

		return jumps;
	}

	return dfs(0);
};

console.log(jump([2,3,1,1,4]))
