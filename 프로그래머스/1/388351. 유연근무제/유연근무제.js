function solution(schedules, timelogs, startday) {
    let cnt = schedules.length;
    
    for (let i = 0; i < timelogs.length; i++) {
        // 100으로 나눴을때 나머지가 60 이상이면 40을 더합니다.
        let limit = schedules[i] + 10;
        const remain = limit % 100;
        
        if (remain >= 60) limit += 40;
        
        for (let j = 0; j < timelogs[i].length; j++) {
            // 6(토), 7(일) 은 제외합니다.
            const day = ((startday - 1 + j) % 7) + 1; 
            if (day === 6 || day === 7) continue;
            
            if (timelogs[i][j] > limit) {
                cnt--;
                break;
            }
        }
    }
    
    return cnt;
}