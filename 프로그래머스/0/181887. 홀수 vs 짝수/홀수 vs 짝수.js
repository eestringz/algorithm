function solution(num_list) {
    const odd = num_list.filter((_,idx) => idx % 2 === 0).reduce((acc, cur) => acc + cur, 0);
    const even = num_list.filter((_,idx) => idx % 2 != 0).reduce((acc, cur) => acc + cur, 0);
    
    return Math.max(odd, even);
}