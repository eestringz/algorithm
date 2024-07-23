from collections import Counter

def solution(k, tangerine):
    answer = 0
    count_dic = Counter(tangerine)
    sort_lst = sorted(count_dic.items(), key=lambda x: -x[1])

    sum = 0
    for item in sort_lst:
        sum += item[1]
        answer += 1
        if sum >= k: break

    return answer
