function solution(x, n) {
    const answer = [];
    let y = x
    for (let i = 0; i < n; i++) {
        answer.push(y)
        y += x
    }
    return answer;
}