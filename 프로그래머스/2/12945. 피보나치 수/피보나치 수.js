function solution(n) {
    if (n === 1 || n === 0) {
        return n;
    }
    
    return solution(n - 1) % 1234567 + solution(n - 2) % 1234567;
}
