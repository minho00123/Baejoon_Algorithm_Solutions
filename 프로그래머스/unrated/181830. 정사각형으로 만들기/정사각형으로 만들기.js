function solution(arr) {
    const width = arr[0].length;
    const height = arr.length;
    
    if (width === height) {
        return arr;
    } else if (width > height) {
        for (let i = height; i < width; i++) {
            arr.push([]);
            for (let j = 0; j < width; j++) {
                arr[i].push(0);
            }
        }
        return arr;
    } else {
        for (let i = 0; i < height; i++) {
            for (let j = width; j < height; j++) {
                arr[i].push(0);
            }
        }
        return arr;
    }
}