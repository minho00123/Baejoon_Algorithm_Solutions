function solution(M, N) {
    let answer = 0;
    
    if (M === 1 && N === 1) {
        return answer;
    }
    
    const minimumNumber = Math.min(M, N);
    answer += minimumNumber - 1;
    if (M === minimumNumber) {
        answer += (N - 1) * minimumNumber;
    } else {
        answer += (M - 1) * minimumNumber;
    }
    
    return answer;
}