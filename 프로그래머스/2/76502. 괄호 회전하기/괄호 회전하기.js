function isValid(arr) {
    const stack = [];
    
	for (const char of arr) {
        if (char === "(" || char === "[" || char === "{") {
            stack.push(char);
        } else {
			if (stack.length === 0) {
                return false;
            } else {
                const top = stack.pop();
                
                if (top === "(" && char === ")") {
                    continue;
                } else if (top === "[" && char === "]") {
                    continue;
                } else if (top === "{" && char === "}") {
                    continue;
                } else {
                    return false;
                }
            }
        }
    }
    
    return stack.length === 0;
}

function solution(s) {
    let answer = 0;
    const arr = s.split("");
	
    for (let i = 0; i < arr.length; i++) {
        if (isValid(arr)) {
            answer++;
        }
        
        const char = arr.shift();
        
        arr.push(char);
    }

    return answer;
}