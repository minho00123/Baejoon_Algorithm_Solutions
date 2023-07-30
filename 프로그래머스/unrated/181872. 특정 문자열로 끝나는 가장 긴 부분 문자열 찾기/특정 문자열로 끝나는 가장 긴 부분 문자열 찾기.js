function solution(myString, pat) {
    let answer = '';
    let idx = myString.lastIndexOf(pat)
    for (let i = 0; i < idx + pat.length; i++) {
        answer += myString[i]
    }
    return answer;   
}