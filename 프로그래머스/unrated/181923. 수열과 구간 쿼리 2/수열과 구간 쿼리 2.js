function solution(arr, queries) {
    let answer = [];
    for (let i = 0; i < queries.length; i++) {
        let s = queries[i][0];
        let e = queries[i][1];
        let k = queries[i][2];
        
        let findNumber = 10000000;
        for (let j = 0; j < arr.length; j++) {
            if(j >= s && j <= e) {
                if (arr[j] > k && arr[j] < findNumber) {
                    findNumber = arr[j];
                }
            }   
        }
        if (findNumber === 10000000) {
            findNumber = -1;
        }
        answer.push(findNumber);
        
    }
    return answer;
}