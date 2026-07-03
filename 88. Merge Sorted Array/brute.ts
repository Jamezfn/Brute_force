/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
	for (let i = 0; i < n; i++) {
		nums1[m + i] = nums2[i];
	}

	nums1.sort((a, b) => a - b);
};

const nums1 = [1,2,3,0,0,0];
const m = 3;
const nums2 = [2,5,6];
const n = 3;
merge(nums1, m, nums2, n);

console.log(nums1);
