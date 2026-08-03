function maxTurbulenceSize(arr: number[]): number {
	const n = arr.length;

	if (n === 1) return 1;

	let ans = 1;
	for (let i = 0; i < n; i++) {
		let l = 1;
		let prev = 0

		for (let j = i + 1; j < n; j++) {
			let curr: number;
			if (arr[j - 1] < arr[j]) {
				curr = 1;
			}
			else if (arr[j - 1] > arr[j]) {
				curr = -1;
			}
			else {
				break;
			}

			if (prev === 0 || prev !== curr) {
				l++;
				ans = Math.max(ans, l);
				prev = curr;
			} else {
				break
			}
		}
	}


	return ans;
};


console.log(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]));
