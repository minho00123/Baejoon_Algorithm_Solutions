function solution(arr) {
    let answer = [];
    let firstIdx = -1;
    let lastIdx = -1;
    
    for (let i = 0; i < arr.length; i++) {
        if (firstIdx === -1 && arr[i] === 2) {
            firstIdx = i;
        } else if (firstIdx != -1 && arr[i] === 2) {
            lastIdx = i;
        }
    }
    
    
    if (firstIdx === -1) {
        answer.push(-1);
    } else if (firstIdx != -1 && lastIdx === -1) {
        answer.push(2);
    } else {
        for (let i = firstIdx; i <= lastIdx; i++) {
            answer.push(arr[i]);
        }
    }
    
    return answer;
}