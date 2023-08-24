function solution(polynomial) {
    let xCount = 0;
    let constant = 0;
    const numArr = polynomial.split(' ');
    for (let i = 0; i < numArr.length; i += 2) {
        if (numArr[i].indexOf('x') != -1) {
            if (numArr[i].length === 1) {
                xCount++;
            } else {
                let tmp = numArr[i].split('x');
                xCount += parseInt(tmp[0])
            }
        } else {
            constant += parseInt(numArr[i]);
        }
    }
    if (xCount === 0) return `${constant}`;
    else if (constant === 0 && xCount === 1) return `x`;
    else if (constant === 0) return `${xCount}x`;
    else if (xCount === 1) return `x + ${constant}`;
    else return `${xCount}x + ${constant}`
}