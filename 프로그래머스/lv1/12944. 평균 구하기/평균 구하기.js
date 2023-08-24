function solution(arr) {
    let total = 0;
    let length = arr.length;
    arr.forEach(number => total += number);
    return total / length;
}