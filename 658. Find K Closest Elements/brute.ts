function findClosestElements(arr: number[], k: number, x: number): number[] {
	const nums: [number, number][] = [];
	for (const num of arr) {
		nums.push([Math.abs(num - x), num]);
	}

	nums.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

	const res: number[] = [];
	for (let i = 0; i < k; i++) {
		res.push(nums[i][1]);
	}
	
	res.sort((a, b) => a - b);
	return res;
};

console.log(findClosestElements([1,2,3,4,5], 4, 3));
