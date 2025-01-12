function solution(answers) {
    const lst_1 = [1, 2, 3, 4, 5];
    const lst_2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const lst_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const counts = [0, 0, 0];
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === lst_1[i % lst_1.length]) counts[0]++;
        if (answers[i] === lst_2[i % lst_2.length]) counts[1]++;
        if (answers[i] === lst_3[i % lst_3.length]) counts[2]++;
    }
    
    const max_value = Math.max(...counts);
    
    return counts
        .map((value, idx) => value === max_value ? idx + 1 : null)
        .filter(value => value != null);
}
