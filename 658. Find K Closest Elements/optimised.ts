function findClosestElements(arr: number[], k: number, x: number): number[] {
	let [l, r] = [0, arr.length];
	while (l < r) {
		const mid = Math.floor((l + r) / 2);
		if (x - arr[mid] > arr[mid + k] - x) {
			l = mid + 1;
		} else {
			r = mid;
		}
	}

	return arr.slice(l, l + k);
};

console.log(findClosestElements([1,2,3,4,5], 4, 3));
