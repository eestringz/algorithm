def solution(elements):
    answer = set()
    lst = elements * 2

    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(lst[i:i + j + 1]))

    return len(answer)