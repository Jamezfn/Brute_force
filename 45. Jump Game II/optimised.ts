function jump(nums: number[]): number {   
	const len = nums.length;

	let res = 0;

	let l = 0;
	let r = 0;

	while (r < len - 1) {
		let far = 0;

		for (let i = l; i <= r; i++) {
			far = Math.max(far, i + nums[i]);
		}

		l = r + 1;
		r = far;

		res++;
	}

	return res;
};

console.log(jump([2,3,1,1,4]));
