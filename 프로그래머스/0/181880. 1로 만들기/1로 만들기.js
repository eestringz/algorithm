function solution(num_list) {
    let cnt = 0;
    
    for (let num of num_list) {
        while (num > 1) {
            cnt ++;
            num = Math.floor(num / 2);
        }
    }
    
    return cnt;
}
