function solution(arr, k) {
    const answer = [];
    
    for (let i = 0; answer.length !== k; i++) {
        if (i >= arr.length - 1) {
            answer.push(-1);
        } else if (arr[i] !== answer[answer.length-1]) {
            answer.push(arr[i]);
        }
    }
    
    return answer;
}