function canJump(nums: number[]): boolean {
	const n = nums.length;

	function dfs(i){
		if (i >= n - 1) return true;

		for (let j = 1; j <= nums[i]; j++) {
			if (dfs(i + j)) return true;
		}

		return false;
	}

	return dfs(0);
};

console.log(canJump([2,3,1,1,4]));
console.log(canJump([3,2,1,0,4]));
