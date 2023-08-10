function solution(balls, share) {
    let nFact = 1;
    let nmFact = 1;
    let mFact = 1;
    for (let i = 1; i < balls + 1; i++) {
        nFact *= i;
    }
    for (let i = 1; i < balls - share + 1; i++) {
        nmFact *= i;
    }
    for (let i = 1; i < share + 1; i++) {
        mFact *= i;
    }
    const answer = Math.round(nFact / (nmFact * mFact))
    
    return answer;
}