function solution(my_string) {
    const numberArray = my_string.split(' ');
    let answer = Number(numberArray[0]);

    for (let i = 1; i < numberArray.length; i += 2) {
        if (numberArray[i] === '+') {
            answer += Number(numberArray[i+1]);
        } else if (numberArray[i] === '-') {
            answer -= Number(numberArray[i+1]);
        }
    }
    
    return answer;
}