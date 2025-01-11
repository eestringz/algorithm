function solution(a, b, c) {
    const dice = new Set([a, b, c]);
    
    const sum = a + b + c;
    const squareSum = a ** 2 + b ** 2 + c ** 2;
    const cubeSum = a ** 3 + b ** 3 + c ** 3;
    
    if (dice.size === 3) {
        return sum;
    } else if (dice.size === 2) {
        return sum * squareSum;
    } else {
        return sum * squareSum * cubeSum;
    }
}
