const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let answer = '';
    
    for (let i = 0; i < str.length; i++) {
        let asciiNumber = str[i].charCodeAt();
        if (asciiNumber >= 65 && asciiNumber <= 90) {
            answer += String.fromCharCode(asciiNumber + 32);
        } else {
            answer += String.fromCharCode(asciiNumber - 32);
        }
    }
    console.log(answer);
});