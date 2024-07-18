function solution(n, left, right) {
    const answer = [];

    for (let i = left; i <= right; i++) {
        const r = Math.floor(i / n);
        const c = i % n;
        
        answer.push(Math.max(r, c) + 1);
    }
    
    return answer;
}