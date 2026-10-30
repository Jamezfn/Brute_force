function fruitIntoBaskets(fruits: number[]): number {
	let max_fruits: number = 0;
	const state: Map<number, number> = new Map();
	let start: number = 0;

	for (let end = 0; end < fruits.length; end++) {
		state.set(fruits[end], (state.get(fruits[end]) ?? 0) + 1);

		while (state.size > 2) {
			state.set(fruits[start], state.get(fruits[start])! - 1);

			if (state.get(fruits[start]) === 0) {
				state.delete(fruits[start]);
			}

			start++;
		}

		max_fruits = Math.max(max_fruits, end - start + 1);
	}

	return max_fruits;
}

console.log(fruitIntoBaskets([3, 3, 2, 1, 2, 1, 0]));