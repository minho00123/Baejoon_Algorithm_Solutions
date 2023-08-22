function solution(babbling) {
    const newArr = [];
    for (let i = 0; i < babbling.length; i++) {
        newArr.push(babbling[i].replace(/aya|ye|woo|ma/g, ''));
    }
    let answer = 0;
    for (let i = 0; i < newArr.length; i++) {
        if (newArr[i].length === 0) {
            answer++;
        }
    }
    return answer;
}