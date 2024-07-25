function solution(participant, completion) {
    participant.sort();
    completion.sort();

    const hash = {};

    for (let i = 0; i < completion.length; i++) {
        hash[i] = completion[i];
    }

    for (let i = 0; i < participant.length; i++) {
        if (hash[i] !== participant[i]) {
            return participant[i];
        }
    }
}