function removeDuplicates(nums: number[]): number {
	const n = nums.length;

	if (n <= 2) return n;

	let k = 2;

	for (let i = 2; i < n; i++) {
		if (nums[i] !== nums[k - 2]) {
			nums[k] = nums[i];
			k++;
		}
	}

	return k;
};

console.log(removeDuplicates([1,1,1,2,2,3]));
