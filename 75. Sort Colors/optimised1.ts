function sortColors(nums: number[]): void {
	let [l, r] = [0, nums.length - 1];

	let i = 0;

	function swap(i: number, j: number): void {
		[nums[i], nums[j]] = [nums[j], nums[i]];
	}

	while (i <= r) {
		if (nums[i] === 0) {
			swap(l, i);
			l++;
		}
		else if (nums[i] === 2) {
			swap(i, r);
			r--;
			i--;
		}

		i++;
	}
};

const nums = [2,0,2,1,1,0];
sortColors(nums);
console.log(nums);
