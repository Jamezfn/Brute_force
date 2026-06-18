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

	return arr[l: l + k];
};
