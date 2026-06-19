function searchRange(nums: number[], target: number): number[] {
	const res: number[] = [];
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] === target) {
			res.push(i);
		}
	}

	return res;
};

console.log(searchRange([5,7,7,8,8,10], 8))
