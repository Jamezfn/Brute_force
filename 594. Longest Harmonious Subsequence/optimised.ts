function findLHS(nums: number[]): number {
	const n = nums.length;
	const f = new Map<number, number>();
	for (const num of nums) {
		f.set(num, (f.get(num) || 0) + 1);
	}

	let ans = 0;
	for (const [num, count] of f) {
		if (f.has(num + 1)) {
			ans = Math.max(ans, count + f.get(num + 1));
		}
	}

	return ans
};

console.log(findLHS([1, 2, 5, 6, 6]));
