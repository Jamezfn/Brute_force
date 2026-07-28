function isPalindrome(s: string): boolean {
	let clean = "";

	for (const char of s) {
		if (/[a-zA-Z0-9]/.test(char)) {
			clean += char.toLowerCase();
		}
	}

	return clean == clean.split("").reverse().join("")
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
