function twoSum(numbers: number[], target: number): number[] {
	let [l, r] = [0, numbers.length - 1];

	while (l < r) {
		let sm = numbers[l] + numbers[r];

		if (sm > target) {
			r--;
		}
		else if (sm < target) {
			l++;
		}
		else {
			return [l + 1, r + 1];
		}
	}

	return [];
};

console.log(twoSum([2,7,11,15], 9));

