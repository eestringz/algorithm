from collections import deque


def bfs(y, x):
    global used
    q = deque()
    q.append([y, x])
    used[y][x] = 1
    size = 1
    while q:
        yy, xx = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dx > n - 1 or dy > m - 1: continue
            if used[dy][dx] == 1: continue
            if arr[dy][dx] == arr[yy][xx]:
                used[dy][dx] = 1
                q.append([dy, dx])
                size += 1

    return size ** 2


n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
used = [[0] * n for _ in range(m)]
ret_W, ret_B = 0, 0
for i in range(m):
    for j in range(n):
        if used[i][j] == 0:
            if arr[i][j] == 'W':
                ret_W += bfs(i, j)
            else:
                ret_B += bfs(i, j)

print(ret_W, ret_B)