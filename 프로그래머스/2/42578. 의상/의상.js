function solution(clothes) {
    let count = 1;
    const types = {}
    
    for (const clothe of clothes) {
        const [name, type] = clothe;
        
        if (types[type]) {
            types[type]++;
        } else {
            types[type] = 1;
        }
    }

    for (const key in types) {
        count *= types[key] + 1;
    }
    
    return count - 1;
}