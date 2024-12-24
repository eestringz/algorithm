function solution(myString) {
    const str = myString.replaceAll('a', 'A')
    
    return str
        .split('')
        .map(char => (char > 'A' && char <= 'Z' ? char.toLowerCase() : char))
        .join('');

}