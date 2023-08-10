function solution(sides) {
    let answer = 0;
    const minNumber = Math.min(...sides);
    const maxNumber = Math.max(...sides);
    
    for (let i = maxNumber + 1; i < minNumber + maxNumber; i++) {
        answer++;
    }
    
    for (let i = 1; i <= maxNumber; i++) {
        if (minNumber + i > maxNumber) {
            answer++;
        }
    }
    
    return answer;
}