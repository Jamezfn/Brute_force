function search(nums: number[], target: number): number {
        const len = nums.length;
	let [l, r] = [0, len - 1];

	while (l < r) {
		const mid = Math.floor((l + r) / 2);
		if (nums[mid] === target) return mid;
		if (nums[l] === target) return l;
		if (nums[r] === target) return r;

		if (nums[l] <= nums[mid]) {
			if (nums[l] < target && target < nums[mid]) {
				r = mid - 1;
			} else {
				l = mid + 1;
			}
		} else {
			if (nums[mid] < target && target < nums[r]) {
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
	}
};

console.log(search([4,5,6,7,0,1,2], 0));
console.log(search([8,1,2,3,4,5,6,7], 6));
