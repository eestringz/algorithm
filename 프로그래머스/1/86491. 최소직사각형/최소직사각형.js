function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;

    for (const [w, h] of sizes) {
        // 명함을 회전하여 더 긴 쪽을 가로로 설정
        const [larger, smaller] = w > h ? [w, h] : [h, w];
        
        // 가장 긴 가로와 세로 길이를 추적
        maxWidth = Math.max(maxWidth, larger);
        maxHeight = Math.max(maxHeight, smaller);
    }

    return maxWidth * maxHeight;
}
