function solution(nums) {
    const set = new Set(nums);
    const limit = nums.length / 2;
    
    return Math.min(set.size, limit);
}