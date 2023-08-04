function solution(myStr) {
    let answer = [];
    let tmp = [];
    let reg = /a|b|c/
    tmp = myStr.split(reg);
    for (let i = 0; i < tmp.length; i++) {
        if (tmp[i] != '') {
            answer.push(tmp[i]);
        }
    }
    if (answer.length == 0) {
        return ["EMPTY"];
    } else {
        return answer;
    }
}