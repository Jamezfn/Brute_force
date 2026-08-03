function maxTurbulenceSize(arr: number[]): number {
	let [l, r] = [0, 1];
	let [res, prev] = [1, ""];

	while (r < arr.length) {
		if (arr[r - 1] > arr[r] && prev !== ">") {
			res = Math.max(res, r - l + 1);
			r++;
			prev = ">"
		}
		else if (arr[r - 1] < arr[r] && prev !== "<") {
			res = Math.max(res, r - l + 1);
			r++;
			prev = "<"
		}
		else {
			if (arr[r - 1] === arr[r]) {
				r = r + 1;
			}
			l = r - 1;
			prev = ""
		}
	}

	return res;
}

console.log(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]));