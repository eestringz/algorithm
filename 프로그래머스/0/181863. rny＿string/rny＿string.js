function solution(rny_string) {
    let answer = '';
    
    for (let str of rny_string) {
        if (str === 'm') {
            answer += 'rn';
        } else {
            answer += str;
        }
    }
    
    return answer;
}
