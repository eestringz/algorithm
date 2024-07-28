from collections import deque


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        y, x = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy, dx = (y + dty[i]) % n, (x + dtx[i]) % m
            if not visited[dy][dx] and arr[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append([dy, dx])


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
