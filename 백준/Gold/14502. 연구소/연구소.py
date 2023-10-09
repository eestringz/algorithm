import sys
import copy

input = sys.stdin.readline
from collections import deque


def bfs():
    global ans
    # 원래의 arr은 유지시켜야 하므로 deepcopy
    mapp = copy.deepcopy(arr)
    # 현재 모든 바이러스 큐에 담기
    q = deque()
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 2:
                q.append([i, j])
    # 바이러스 감염시키기
    while q:
        y, x = q.popleft()
        dty = [-1, 0, 1, 0]
        dtx = [0, 1, 0, -1]
        for i in range(4):
            dy = y + dty[i]
            dx = x + dtx[i]
            if dx < 0 or dy < 0 or dx > m - 1 or dy > n - 1: continue
            if mapp[dy][dx] == 0:
                mapp[dy][dx] = 2
                q.append([dy, dx])
    # 감염 되지 않은 곳의 최댓값 구하기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                cnt += 1
    ans = max(ans, cnt)


# 벽 세우기 (브루트포스 algo) -> 벽을 3개 세우면 bfs 실행
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:  # 빈 공간이면, 벽 세우기 가능
                arr[i][j] = 1  # 벽 세우고
                wall(cnt + 1)  # 다시 두 번째 벽 세우러 가기
                arr[i][j] = 0  # 다시 벽 허물기 (백트래킹)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
wall(0)
print(ans)