function solution(dots) {
    let maxWidth = -1;
    let maxHeight = -1;
    for (let i = 0; i < 3; i++) {
        let width = Math.abs(dots[i][0] - dots[i+1][0]);
        let height = Math.abs(dots[i][1] - dots[i+1][1]);
        if (width > maxWidth) {
            maxWidth = width;
        }
        if (height > maxHeight) {
            maxHeight = height;
        }
    }
    
    return maxWidth * maxHeight;
}