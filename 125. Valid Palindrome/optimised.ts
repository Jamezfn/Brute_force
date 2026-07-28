function isPalindrome(s: string): boolean {
        const isAlnum = (char: string): boolean => /[a-zA-Z0-9]/.test(char);

	let [l, r] = [0, s.length - 1];

	while (l < r) {
		while (l < r && !isAlnum(s[l])) {
			l++;
		}

		while (r > l && !isAlnum(s[r])) {
                        r--;
                }

		if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;

		l++;
		r--;
	}

	return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
