def solution(array, commands):
    answer = []

    for it in commands:
        i, j, k = it[0], it[1], it[2]
        answer.append(sorted(([0] + array)[i:j + 1])[k - 1])

    return answer