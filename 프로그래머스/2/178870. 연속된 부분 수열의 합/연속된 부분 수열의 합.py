def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    s = e = 0
    sum = sequence[0]
    while True:
        if sum < k:
            e += 1
            if e == len(sequence): break
            sum += sequence[e]
        else:
            if sum == k:
                if e - s < answer[1] - answer[0]:
                    answer = [s, e]
            sum -= sequence[s]
            s += 1

    return answer