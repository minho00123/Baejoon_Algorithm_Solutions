function solution(progresses, speeds) {
    const answer = [];
    const days = [];
    
    for (let i = 0; i < progresses.length; i++) {
        days.push(Math.ceil((100 - progresses[i]) / speeds[i]));
    }

    let count = 0;
    let frontDay = days[0];
    
    for (let i = 0; i < days.length; i++) {
        if (days[i] <= frontDay) {
            count++;
        } else {
            answer.push(count);
            count = 1;
            frontDay = days[i];
        }
    }

    answer.push(count);
    
    return answer;
}