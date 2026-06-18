function search(nums: number[], target: number): number {
	const len = nums.length;

	for (let i = 0; i < len; i++) {
		if (nums[i] === target) {
			return i;
		}
	}
};

console.log(search([4,5,6,7,0,1,2], 0));
