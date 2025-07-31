#!/usr/bin/env node

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
        const sign = (dividend < 0) !== (divisor < 0);
        let dvd = Math.abs(dividend);
        const dvs = Math.abs(divisor);

        let quotient = 0;
        while (dvd >= dvs) {
		let temp = dvs;
		let multiple = 1;
		while ((temp << 1) <= dvd) {
			temp <<= 1;
			multiple <<= 1;
		}
		dvd -= temp;
		quotient += multiple;
	}
	if (sign) {
		quotient = -quotient;
	}
        const MAX_INT = 2 ** 31 - 1;
	const MIN_INT = -(2 ** 31);
	return Math.min(Math.max(MIN_INT, quotient), MAX_INT);
};
console.log(divide(-10, -2));
console.log(divide(7, -3));
console.log(divide(-15, 4));
