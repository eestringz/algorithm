function solution(participant, completion) {
    const obj = new Object();
    
    for (let i = 0; i < participant.length; i++) {
        if (participant[i] in obj) {
            obj[participant[i]] += 1
        } else {
            obj[participant[i]] = 1
        }
    }
    
        
    for (let i = 0; i < completion.length; i++) {
        obj[completion[i]] -= 1
    }
    

    for (let key in obj) {
        if (obj[key] > 0) {
            return key
        }
    }

}