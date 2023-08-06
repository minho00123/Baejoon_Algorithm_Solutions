function solution(strArr) {
    let answer = 0;
    let arr = [];
    
    for (let i = 0; i < 30; i++) {
        arr.push(0);
    }
    
    for (let i = 0; i < strArr.length; i++) {
        arr[strArr[i].length - 1] ++
    }
    
    for (let i = 0; i < 30; i++) {
        if (answer < arr[i]) {
            answer = arr[i];
        }
    }
    
    return answer;
}