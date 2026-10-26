class TimeMap {
	private store: Map<string, [string, number][]>;

	constructor() {
		this.store = new Map();
	}

	set(key: string, value: string, timestamp: number) {
		if (!this.store.has(key)) {
			this.store.set(key, []);
		}

		this.store.get(key)!.push([value, timestamp]);
	}

	get(key: string, timestamp: number) {
		const values = this.store.get(key) ?? [];
		let res = "";

		let [l, r] = [0, values.length - 1];

		while (l <= r) {
			const m = Math.floor((l + r) / 2);
		
			if (values[m][1] <= timestamp) {
				res = values[m][0];
				l = m + 1;
			} else {
				r = m - 1;
			}

		}
		
		return res;
	}
}

// Usage
const timeMap = new TimeMap();

timeMap.set("foo", "bar", 1);
timeMap.set("foo", "bar2", 4);

console.log(timeMap.get("foo", 1)); // bar
console.log(timeMap.get("foo", 3)); // bar
console.log(timeMap.get("foo", 4)); // bar2
console.log(timeMap.get("foo", 5)); // bar2
