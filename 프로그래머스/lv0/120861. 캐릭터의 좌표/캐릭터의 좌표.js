function solution(keyinput, board) {
    let answer = [0, 0];
    for (let i = 0; i < keyinput.length; i++) {
        if (keyinput[i] === 'up') {
            if (answer[1] < parseInt(board[1]/2)) {
                answer[1]++;
            }
        } else if (keyinput[i] === 'down') {
            if (answer[1] > -parseInt(board[1]/2)) {
                answer[1]--;
            }
        } else if (keyinput[i] === 'left') {
            if (answer[0] > -parseInt(board[0]/2)) {
                answer[0]--;
            }
        } else if (keyinput[i] === 'right') {
            if (answer[0] < parseInt(board[0]/2)) {
                answer[0]++;
            }
        }
    }
    return answer;
}