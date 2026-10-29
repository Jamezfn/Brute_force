function maxScore(cards: number[], k: number): number {
    const total: number = cards.reduce((sum, card) => sum + card, 0);

    if (k === cards.length) {
	    return total;
    }

    let state: number = 0;
    let maxPoints: number = 0;
    let start: number = 0;

    for (let end = 0; end < cards.length; end++) {
	    state += cards[end];

	    if (end - start + 1 === cards.length - k) {
		    maxPoints = Math.max(total - state, maxPoints);
		    state -= cards[start];
		    start++;
	    }
    }

    return maxPoints;
}

console.log(maxScore([2,11,4,5,3,9,2], 3))
