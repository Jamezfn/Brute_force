/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
	let i = m - 1;
	let j = n - 1;
	let l = m + n - 1;

	while (i >= 0 && j >= 0) {
		if (nums1[i] > nums2[j]) {
			nums1[l] = nums1[i];
			i--;
		} else {
			nums1[l] = nums2[j];
			j--;
		}

		l--;
	}

	while (j >= 0) {
		nums1[l] = nums2[j];
		j--;
		l--;
	}
};

const nums1 = [1,2,3,0,0,0];
const m = 3;
const nums2 = [2,5,6];
const n = 3;
merge(nums1, m, nums2, n);

console.log(nums1);
