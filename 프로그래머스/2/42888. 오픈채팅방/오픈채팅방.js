function solution(record) {
    const answer = [];
    const info = {};

    for (const item of record) {
        const [command, id, name] = item.split(" ");

        if (command === "Enter") {
            info[id] = name;
        } else if (command === "Change") {
            info[id] = name;
        }
    }
    
    for (const item of record) {
        const [command, id] = item.split(" ");
        
        if (command === "Enter") {
            answer.push(`${info[id]}님이 들어왔습니다.`);
        } else if (command === "Leave") {
            answer.push(`${info[id]}님이 나갔습니다.`);
        }
    }

    return answer;
}