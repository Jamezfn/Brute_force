function minimumDifference(nums: number[], k: number): number {
	nums.sort((a, b) => a - b);

	let res = Infinity;

	for (let i = 0; i <= nums.length - k; i++) {
		res = Math.min(res, nums[i + k - 1] - nums[i])
	}

	return res;
};

console.log(minimumDifference([9,4,1,7], 2))
