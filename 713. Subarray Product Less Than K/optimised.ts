function numSubarrayProductLessThanK(nums: number[], k: number): number {
	const n = nums.length;
	if (k < 1) return 0;

	let count: number = 0;
	let product: number = 1;
	let i = 0;
	for (let j = 0; j < n; j++){
		product *= nums[j];

		while (i <= j && product >= k) {
			product = Math.floor(product / nums[i]);
			i++;
		}

		count += j - i + 1;
	}

	return count;
};

console.log(numSubarrayProductLessThanK([10,5,2,6], 100))
console.log(numSubarrayProductLessThanK([1,2,3], 0))
