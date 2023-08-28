function solution(n)
{
    let answer = 0;
    const nStr = String(n);
    for (let i = 0; i < nStr.length; i++) {
        answer += parseInt(nStr[i])
    }
    return answer;
}