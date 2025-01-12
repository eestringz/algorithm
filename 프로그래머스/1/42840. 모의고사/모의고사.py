import math

def solution(answers):
    lst_1 = [1, 2, 3, 4, 5] * math.ceil(len(answers) / 5)
    lst_2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers) / 8)
    lst_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers) / 10)
    
    counts = {1: 0, 2: 0, 3: 0}
    
    for i in range(len((answers))):
        if answers[i] == lst_1[i]:
            counts[1] += 1
        if answers[i] == lst_2[i]:
            counts[2] += 1
        if answers[i] == lst_3[i]:
            counts[3] += 1
    
    max_value = max(counts.values())
    result = [key for key, value in counts.items() if value == max_value]
    result.sort()

    return result            
        