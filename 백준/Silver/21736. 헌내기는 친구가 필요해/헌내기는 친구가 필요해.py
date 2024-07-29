from collections import deque


def bfs(i, j):
    cnt = 0
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    dty = [-1, 0, 1, 0]
    dtx = [0, 1, 0, -1]

    while q:
        y, x = q.popleft()
        for i in range(4):
            dy, dx = y + dty[i], x + dtx[i]
            if dy < 0 or dx < 0 or dy > n - 1 or dx > m - 1: continue
            if arr[dy][dx] == 'X' or visited[dy][dx] == 1: continue
            if arr[dy][dx] == 'P':
                cnt += 1
            visited[dy][dx] = 1
            q.append([dy, dx])

    return cnt if cnt > 0 else 'TT'


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            print(bfs(i, j))
