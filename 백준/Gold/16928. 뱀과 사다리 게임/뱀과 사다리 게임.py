import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append([1, 0])
    used = [0] * 101
    used[1] = 1
    while q:
        x, cnt = q.popleft()
        if x == 100:
            return cnt

        for k in range(1, 7):
            if x + k > 100: break
            xx = arr[x + k]
            if xx > 100: continue
            if used[xx] == 1: continue
            used[xx] = 1
            q.append([xx, cnt + 1])


n, m = map(int, input().split())
arr = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    arr[a] = b
print(bfs())