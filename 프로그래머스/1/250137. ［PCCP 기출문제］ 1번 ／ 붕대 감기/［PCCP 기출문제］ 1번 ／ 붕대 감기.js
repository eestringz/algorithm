function solution(bandage, health, attacks) {
    const [t, x, y] = bandage;
    
    let cur = health;
    let prev = 0;
    let success = 0;
    
    for (const [at, dmg] of attacks) {
        const delta = at - prev - 1;
        
        if (delta > 0) {
            let total = success + delta;
            cur += delta * x + Math.floor(total / t) * y;
            cur = Math.min(health, cur);
            total = success % t;
        }
        
        cur -= dmg;
        if (cur <= 0) return -1;
        
        prev = at;
        success = 0;
    } 
    
    return cur;
}