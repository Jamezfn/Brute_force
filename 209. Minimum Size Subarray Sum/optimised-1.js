/**
 * @param { number } target
 * @param { number[] } nums
 * @return { number }
 */

var minSubArrayLen = function(target, nums) {
	const n = nums.length;
	const prefix = new Array(n + 1).fill(0);

	for (let i = 0; i < n; i++) {
		prefix[i + 1] = prefix[i] + nums[i];
	}

	let ans = Infinity;

	for (let i = 0; i < n; i++) {
		const needed = target + prefix[i];

		let lo = i + 1, hi = n;

		while (lo <= hi) {
			const mid = (lo + hi) >> 1;

			if (prefix[mid] >= needed) {
				hi = mid - 1;
			} else {
				lo = mid + 1;
			}
		}

		if (lo <= n) {
                     	ans = Math.min(ans, lo - i);
		}
	}

	return ans === Infinity ? 0 : ans;
};

console.log(minSubArrayLen(4, [2,3,1,2,4,3]));

