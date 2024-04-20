function solution(s)
{
    const arr = s.split("");
    const result = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === result[result.length - 1]) {
            result.pop();
        } else {
            result.push(arr[i]);
        }
    }
    
    return result.length === 0 ? 1 : 0;
}