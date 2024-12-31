function solution(n) {
    if (n % 2 === 1) {
        return Array
            .from({length : Math.ceil(n / 2)}, (_, i) => 2 * i + 1)
            .reduce((acc, cur) => acc + cur, 0);
    } else {
         return Array
            .from({length : n / 2}, (_, i) => 2 * (i + 1))
            .reduce((acc, cur) => acc + cur ** 2, 0);
    }
}
