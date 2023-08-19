function solution(quiz) {
    const answers = [];
    for (let i = 0; i < quiz.length; i++) {
        let charArray = quiz[i].split(' ');
        let num1 = parseInt(charArray[0]);
        let num2 = parseInt(charArray[2]);
        let answer = parseInt(charArray[4]);
        if (charArray[1] === '+') {
            if (num1 + num2 === answer) {
                answers.push('O');
            } else {
                answers.push('X');
            }
        } else {
            if (num1 - num2 === answer) {
                answers.push('O');
            } else {
                answers.push('X');
            }
        }
    }
    return answers;
}