import sys

input = sys.stdin.readline


def solution(i):
    if i in dic:
        return dic[i]
    else:
        dic[i] = solution(i // P) + solution(i // Q)
        return dic[i]


N, P, Q = map(int, input().split())
dic = {}
dic[0] = 1

print(solution(N))
