function solution(s){
    const stack = [];
    
    for (let i = 0; i < s.length; i++) {
        if (stack.length === 0 && s[i] === ")") {
            return false;
        } else if (s[i] === "(") {
            stack.push("(");
        } else if (s[i] === ")" && stack[stack.length - 1] === "(") {
            stack.pop();
        }
    }
    
    if (stack.length === 0) {
        return true;
    } else {
        return false;
    }
}