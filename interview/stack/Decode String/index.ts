function decodeString(s: string): string {
	const stack: (number | string)[] = [];
	let currString: string = "";
	let currNumber: number = 0;

	for (const char of s) {
		if (char === "[") {
			stack.push(currString);
			stack.push(currNumber);
			currString = "";
			currNumber = 0;
		} else if (char === "]") {
			let num: number = stack.pop() as number;
			let prevString: string = stack.pop() as string;
			currString = prevString + currString.repeat(num);
		} else if (/\d/.test(char)) {
			currNumber = currNumber * 10 + parseInt(char)
		} else {
			currString += char;
		}
	}

	return currString;
}

console.log(decodeString("3[a2[c]]"));