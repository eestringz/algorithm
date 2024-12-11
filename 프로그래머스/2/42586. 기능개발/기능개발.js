function solution(progresses, speeds) {
    var answer = [];
    var days = [];

    for (let i = 0; i < progresses.length; i++) {
        const remaining = Math.ceil((100 - progresses[i]) / speeds[i]);
        days.push(remaining);
    }
    
    while (days.length > 0) {
        const current = days.shift();
        let cnt = 1;
        
        while (days.length > 0 && days[0] <= current) {
            days.shift();
            cnt++;
        }
        
        answer.push(cnt);
    }
    
    return answer;
}
