function solution(s) {
    let answer = 0;
    const sArr = s.split(' ');
    for (let i = 0; i < sArr.length; i++) {
        if (sArr[i] == 'Z') {
            answer -= parseInt(sArr[i - 1]);
        } else {
            answer += parseInt(sArr[i]);
        }
    }
    return answer;
}