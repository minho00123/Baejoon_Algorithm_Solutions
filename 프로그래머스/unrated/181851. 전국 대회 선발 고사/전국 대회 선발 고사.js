function solution(rank, attendance) {
    const realRank = [];
    for (let i = 0; i < attendance.length; i++) {
        if (attendance[i]) {
            realRank.push(rank[i]);
        }
    }
    realRank.sort((a, b) => a - b);
    let abcArr = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < rank.length; j++) {
            if (realRank[i] === rank[j]) {
                abcArr.push(j);
            }
        }
    }
    const a = abcArr[0];
    const b = abcArr[1];
    const c = abcArr[2];
    return (10000 * a) + (100 * b) + c;
}