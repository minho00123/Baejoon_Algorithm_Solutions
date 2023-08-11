function solution(str_list) {
    let leftIndex = str_list.indexOf('l');
    let rightIndex = str_list.indexOf('r');
    
    let answer = [];
    
    if (leftIndex === -1 && rightIndex === -1) {
        return answer;
    } else if (leftIndex === -1) {
        for (let i = rightIndex + 1; i < str_list.length; i++) {
            answer.push(str_list[i])
        }
    } else if (rightIndex === -1) {
        for (let i = 0; i < leftIndex; i++) {
            answer.push(str_list[i]);
        }
    } else if (leftIndex < rightIndex) {
        for (let i = 0; i < leftIndex; i++) {
            answer.push(str_list[i]);
        }
    } else {
        for (let i = rightIndex + 1; i < str_list.length; i++) {
            answer.push(str_list[i])
        }
    }
    
    return answer;
}