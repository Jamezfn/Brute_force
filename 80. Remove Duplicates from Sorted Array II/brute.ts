function removeDuplicates(nums: number[]): number {
	let i = 0;
	while (i < nums.length - 2) {
		if (nums[i] === nums[i + 1] && nums[i] === nums[i + 2]) {
			nums.splice(i + 2, 1);
		} else {
			i++
		}
	}

	return nums.length;
};

console.log(removeDuplicates([1,1,1,2,2,3]));
