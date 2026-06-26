function searchInsert(nums: number[], target: number): number {
	let [l, r] = [0, nums.length - 1];
	while (l <= r) {
		let mid = Math.floor((r + l) / 2);
		if (nums[mid] == target) {
			return mid;
		} else if (nums[mid] < target) {
			l = mid + 1;
		} else {
			r = mid - 1;
		}
	}

	return l;
};

console.log(searchInsert([1,3,5,6], 5));
