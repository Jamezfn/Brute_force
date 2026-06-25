function findMaxAverage(nums: number[], k: number): number {
	const n = nums.length;
	let res: number = Number.NEGATIVE_INFINITY;
	for (let i = 0; i <= n - k; i++) {
		let sm = 0;
		for (let j = i; j < i + k; j++) {
			sm += nums[j]
		}

		res = Math.max(res, sm / k);
	}

	return res;
};

console.log(findMaxAverage([1,12,-5,-6,50,3], 4));
