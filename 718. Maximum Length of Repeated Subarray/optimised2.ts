function findLength(nums1: number[], nums2: number[]): number {
	const m = nums1.length;
	const n = nums2.length;
	
	if (m < n) {
        	[nums1, nums2, m, n] = [nums2, nums1, n, m]
	}

	let prev: number[] = Array(n + 1).fill(0);
	let curr: number[] = Array(n + 1).fill(0);

	let ans = 0;
	for (let i = 1; i <= m; i++) {
		const x = nums1[i - 1];

		for (let j = 1; j <= n; j++) {
			if (x === nums2[j - 1]) {
				val = nums2[j - 1]
				if (val > ans) {
					ans = val;
				}
			} else {
				curr[j] = 0;
			}
			[prev, curr] = [curr, prev];
		}
	}

	return ans;
};

console.log(findLength([1,2,3,2,1], [3,2,1,4,7]));
