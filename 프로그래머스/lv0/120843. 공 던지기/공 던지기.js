function solution(numbers, k) {
    let answer = 0;
    const numberLength = numbers.length;
    answer = numbers[((k - 1) * 2) % numberLength]
    return answer;
}