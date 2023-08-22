function solution(score) {
    const average = [];
    const sortedAverage = [];
    for (let i = 0; i < score.length; i++) {
        average.push((score[i][0] + score[i][1]) / 2)
        sortedAverage.push((score[i][0] + score[i][1]) / 2)
    }
    sortedAverage.sort(function(a, b)  {
        return b - a;
    });;
    const set = new Set(sortedAverage);
    const setAverage = [...set]
    
    let rank = 1;
    const answer = [];
    for (let i = 0; i < setAverage.length; i++) {
        let count = 0;
        for (let j = 0; j < average.length; j++) {
            if (setAverage[i] === average[j]) {
                answer[j] = rank;
                count++;
            }
        }
        if (count === 1) {
            rank++;
        } else {
            rank += count;
        }
        
    }
    
    return answer;
}