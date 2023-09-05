import sys
sys.setrecursionlimit(10**7)


def dfs(n):
    global used, cnt
    used[n] = 1
    check.append(n)

    if used[lst[n]] == 1:
        if lst[n] in check:
            cnt -= len(check[check.index(lst[n]):])

    else:
        dfs(lst[n])


T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))     # 인덱스와 차이를 해결하기 위해 처음에 0 추가
    used = [0] * (N + 1)
    cnt = N
    for i in range(1, N + 1):
        check = []              # 사이클을 확인하기 위한 리스트 생성
        if used[i] == 0:
            dfs(i)

    print(cnt)