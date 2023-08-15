function solution(my_string, overwrite_string, s) {
    let stringArray = my_string.split('');
    let j = 0;
    for (let i = s; i < s + overwrite_string.length; i++) {
        stringArray[i] = overwrite_string[j];
        j++;
    }
    let answer = stringArray.join('');
    return answer;
}