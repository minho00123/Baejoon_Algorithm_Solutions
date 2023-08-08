function solution(arr) {
    let answer = 0;
    let tmp = [];
    let cnt = 0;
    let x = 0;
    while (true) {
        tmp = [];
        for (let i = 0; i < arr.length; i++) {
            tmp.push(arr[i]);
        }

        for (let i = 0; i < arr.length; i++) {
            if (arr[i] >= 50 && arr[i] % 2 === 0) {
                arr[i] /= 2;
            } else if (arr[i] < 50 && arr[i] % 2 === 1) {
                arr[i] = arr[i] * 2 + 1;
            }
        }
        
        cnt = 0;
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === tmp[i]) {
                cnt++;
            }
        }

        if (cnt === arr.length) {
            answer = x;
            break;
        }
        x++;
    }
    return answer;
}