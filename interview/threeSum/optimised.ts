function threeSum(nums: number[]): number[][] {
	nums.sort((a, b) => a - b);
	let res = [];

	for (let i = 0; i < nums.length - 2; i++) {
		if (i > 0 && nums[i] === nums[i - 1]) {
			continue;
		}

		let l = i + 1;
		let r = nums.length - 1;

		while (l < r) {
			let tt = nums[i] + nums[l] + nums[r];

			if (tt < 0) {
				l += 1;
			}
			else if (tt > 0) {
				r -= 1;
			}
			else {
				res.push([nums[i], nums[l], nums[r]]);

				while (l < r && nums[l] === nums[l + 1]) {
					l += 1;
				}

				while (l < r && nums[r] === nums[r - 1]) {
                                        r -= 1;
                                }

				l += 1;
				r -= 1;

			}
		}
	}

	return res;
};

console.log(threeSum([-1,0,1,2,-1,-1]));
