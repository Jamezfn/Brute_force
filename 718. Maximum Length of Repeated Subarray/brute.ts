function findLength(nums1: number[], nums2: number[]): number {
	const n = nums1.length;
	const m = nums2.length;

	let ans = 0;
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < m; j++) {
			let l = 0;

			while (i + l < n && j + l < m && nums1[i + l] === nums2[j + l]) {
				l++;
			}

			ans = Math.max(ans, l);
		}
	}

	return ans;
};

console.log(findLength([1,2,3,2,1], [3,2,1,4,7]));
