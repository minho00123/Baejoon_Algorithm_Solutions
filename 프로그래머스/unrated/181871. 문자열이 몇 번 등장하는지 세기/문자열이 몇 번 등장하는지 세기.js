function solution(myString, pat) {
    let answer = 0;
    loop1:
    for (let i = 0; i < myString.length; i++) {
        let cnt = 0;
        let tmp = i;
        for (let j = 0; j < pat.length; j++) {
            if (myString[tmp] == pat[j]) {
                cnt++;
                tmp++;
            } else {
                continue loop1;
            }
        }
        if (cnt == pat.length) answer++;
    }
    return answer;
}