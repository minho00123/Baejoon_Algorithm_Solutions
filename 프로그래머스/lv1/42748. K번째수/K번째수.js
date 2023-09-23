function solution(array, commands) {
    const answer = [];
    for (let i = 0; i < commands.length; i++) {
        let temp = [];
        for (let j = commands[i][0] - 1; j < commands[i][1]; j++) {
            temp.push(array[j]);
        }
        temp.sort(function (a, b) {
            return a - b;
        });
        answer.push(temp[commands[i][2] - 1]);
    }
    return answer;
}