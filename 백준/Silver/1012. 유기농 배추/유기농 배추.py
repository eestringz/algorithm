from collections import deque


def bfs(y, x):
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    while q:
        yy, xx = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dx > M - 1 or dy > N - 1: continue
            if arr[dy][dx] == 1:  # 방문처리 -> 1인 값들을 지날때 0 으로 바꾸기.
                arr[dy][dx] = 0
                q.append([dy, dx])


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)