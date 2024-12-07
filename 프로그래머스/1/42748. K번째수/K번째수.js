function solution(array, commands) {
    let answer = [];
    
    for (let arr of commands) {
        let i = arr[0];
        let j = arr[1];
        let k = arr[2];
        let newArr = array.slice(i - 1, j).sort((a, b) => a - b);
        
        answer.push(newArr[k - 1]);
    }
    
    return answer;
}