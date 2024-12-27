function solution(arr) {
    let X = [];
    
    for (let num of arr) {
        for (let i = 0; i < num; i++) {
            X.push(num);
        } 
    }
    
    return X;
}
