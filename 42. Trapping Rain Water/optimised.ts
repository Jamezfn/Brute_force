function trap(height: number[]): number {
	if (height.length === 0) return 0;

	let l = 0;
	let r =	height.length - 1;
	let maxLeft = height[l];
	let maxRight = height[r];

	let res = 0;

	while (l < r) {
		if (maxLeft < maxRight) {
			l++;
			maxLeft = Math.max(maxLeft, height[l]);
			res += maxLeft - height[l];

		} else {
			r--;
			maxRight =  Math.max(maxRight, height[r]);
			res += maxRight - height[r];
		}
	}

	return res;
};

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
console.log(trap([4,2,0,3,2,5]));
