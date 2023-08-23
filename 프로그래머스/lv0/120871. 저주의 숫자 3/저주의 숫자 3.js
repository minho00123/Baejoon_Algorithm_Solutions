function solution(n) {
    const threeCurse = [];
    for (let i = 1; i <= 200; i++) {
        if (i % 3 === 0) {
            continue;
        } else if (i % 10 === 3) {
            continue;
        } else if ((i % 100 - i % 10) === 30) {
            continue;
        } else if (i >= 30 && i <= 39) {
            continue;
        } else {
            threeCurse.push(i);
        }
    }
    return threeCurse[n-1];
}