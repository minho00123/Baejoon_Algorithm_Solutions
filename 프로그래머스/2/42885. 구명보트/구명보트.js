function solution(people, limit) {
    people.sort((a, b) => a - b);
    
    let count = 0;
    let i = 0;
    
    for (let length = people.length - 1; i < length; length--) {
        if (people[i] + people[length] <= limit) {
            i++;
        }
    }
    
    return people.length - i;
}