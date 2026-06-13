function sortColors(nums: number[]): void {
	const n = nums.length;

	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n - i; j++) {
			if ( nums[j] > nums[j + 1]) {
				[nums[j], nums[j + 1]] = [nums[j + 1], nums[j]]
			}
		}
	}
};

const nums = [2,0,2,1,1,0];
sortColors(nums);
console.log(nums);
