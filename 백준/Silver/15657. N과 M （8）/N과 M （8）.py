def H(now, start):
    if now == M:
        print(*path)
        return

    for i in range(start, N):
        path[now] = lst[i]
        H(now + 1, i)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0] * M
H(0, 0)