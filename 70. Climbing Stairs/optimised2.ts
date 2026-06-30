
function climbStairs(n: number): number {
    let a = 1;
	let b = 1;
	for (let i = 0; i < n - 1; i++) {
		[a, b] = [b, a + b];
	}

	return b;
};

console.log(climbStairs(3));
console.log(climbStairs(4));