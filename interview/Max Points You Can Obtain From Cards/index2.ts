function maxScore(cards: number[], k: number): number {
    const n = cards.length;
    let max_score = 0

    for (let i = 0; i <= k; i++) {
	    const left_sum = cards.slice(0, i).reduce((sum, card) => sum + card, 0);
	    const right_sum = k - i > 0
	    	? cards.slice(n - (k - i)).reduce((sum, card) => sum + card, 0)
		: 0;
	const score = left_sum + right_sum;
	max_score = Math.max(max_score, score); 

    }

    return max_score;
}


console.log(maxScore([2,11,4,5,3,9,2], 3));
