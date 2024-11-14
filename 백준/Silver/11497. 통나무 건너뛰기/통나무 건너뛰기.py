import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    res = lst[1] - lst[0]

    for i in range(len(lst[::2]) - 1):
        res = max(res, lst[::2][i + 1] - lst[::2][i])

    for i in range(len(lst[1::2]) - 1):
        res = max(res, lst[1::2][i + 1] - lst[1::2][i])

    print(res)
