function solution(A, B) {
    if (A === B) {
        return 0;
    }
    
    let answer = -1;
    
    const aArr = A.split('');
    for (let i = 1; i < A.length + 1; i++) {
        let tempChar = aArr.pop();
        aArr.unshift(tempChar);
        let str = aArr.join('');
        if (str === B) {
            return i;
        }
    }
    
    return answer;
}