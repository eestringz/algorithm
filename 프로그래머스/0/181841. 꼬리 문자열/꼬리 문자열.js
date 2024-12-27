function solution(str_list, ex) {
    let result = '';
    for (let str of str_list) {
        if (str.includes(ex)) {
            continue
        }
        
        result += str;
    }
    
    return result;
}
