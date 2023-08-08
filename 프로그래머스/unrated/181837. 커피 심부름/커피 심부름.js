function solution(order) {
    let totalCost = 0;
    for (let i = 0; i < order.length; i++) {
        if (order[i].includes("latte")) {
            totalCost += 5000;
        } else {
            totalCost += 4500;
        }
    }
    return totalCost;
}