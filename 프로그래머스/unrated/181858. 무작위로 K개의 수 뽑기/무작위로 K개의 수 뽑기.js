function solution(arr, k) {
    const answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (answer.length === k) {
            return answer;
        }
        
        if (answer.indexOf(arr[i]) === -1) {
            answer.push(arr[i]);
        }
    }
    
    for (let i = answer.length; i < k; i++) {
        answer.push(-1);
    }
    
    return answer;
}