function solution(num_list) {
    let len = num_list.length;
    
    if (len < 11) {
        let answer = 1;
        for (let i = 0; i < len; i++) {
            answer *= num_list[i];
        }
        
        return answer;
    } else {
        let answer = 0;
        for (let i = 0; i < len; i++) {
            answer += num_list[i];
        }
        
        return answer;
    }
}
