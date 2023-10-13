import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    while q:
        yy, xx = q.popleft()
        dty = [-1, -1, -1, 0, 1, 1, 1, 0]
        dtx = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(8):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx < 0 or dy < 0 or dy > h - 1 or dx > w - 1: continue
            if arr[dy][dx] == 0: continue
            arr[dy][dx] = 0
            q.append([dy, dx])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)