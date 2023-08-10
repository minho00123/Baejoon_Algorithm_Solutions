function solution(my_string) {
    let answer = [];
    for (let i = 0; i < 52; i++) {
        answer.push(0);
    }
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i].charCodeAt() < 97) {
            answer[my_string[i].charCodeAt() - 65]++;
        } else {
            answer[my_string[i].charCodeAt() - 97 + 26]++;
        }
    }
    return answer;
}