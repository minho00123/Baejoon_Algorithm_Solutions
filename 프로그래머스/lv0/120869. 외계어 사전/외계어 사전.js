function solution(spell, dic) {
    let answer = 2;
    const spellLength = spell.length;
    for (let i = 0; i < dic.length; i++) {
        let count = new Array(spellLength).fill(0);
        if (dic[i].length === spellLength) {
            for (let j = 0; j < spellLength; j++) {
                for (let k = 0; k < spellLength; k++) {
                    if (dic[i][j] === spell[k]) {
                        count[k]++;
                    }
                }
            }
            
            let flag = 0;
            for (let j = 0; j < spellLength; j++) {
                if (count[j] !== 1) {
                    flag = 1;
                }
            }
            
            if (flag === 0) {
                answer = 1;
            }
        }
    }
    return answer;
}