function solution(a, b) {
    const monthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
    
    let daysCount = 0;
    
    for (let i = 0; i < a - 1; i++) {
        daysCount += monthDays[i];
    }
    
    daysCount += b;
    
    return days[(daysCount - 1) % 7];
}
