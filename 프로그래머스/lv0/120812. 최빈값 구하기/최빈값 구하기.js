function solution(array) {
    let size = Math.max(...array) + 1;
    let countArray = new Array(size).fill(0);
    for (let i = 0; i < array.length; i++) {
        countArray[array[i]]++;
    }
    
    console.log(countArray)
    
    let answer = 0;
    let count = 0;
    for (let i = 0; i <= countArray.length; i++) {
        if (countArray[i] > count) {
            count = countArray[i];
            answer = i;
        }
    }
    
    let sameNumberCount = 0;
    for (let i = 0; i <= countArray.length; i++) {
        if (count === countArray[i]) {
            sameNumberCount++;
        }
    }
    if (sameNumberCount > 1) {
        return -1;
    }
    return answer;
}