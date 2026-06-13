function sortColors(nums: number[]): void {
	const count = [0, 0, 0];

	for (const num of nums) {
		count[num]++;
	}

	let i = 0;
	for (let c = 0; c < 3; c++) {
		while (count[c] > 0) {
			nums[i] = c;
			i++;
			count[c]--;
		}
	}
};

const nums = [2,0,2,1,1,0];
sortColors(nums);
console.log(nums);
