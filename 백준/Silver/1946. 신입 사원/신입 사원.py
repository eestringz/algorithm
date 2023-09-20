import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])
    cnt = 1
    minn = arr[0][1]
    idx = 1
    while idx < n:
        if arr[idx][1] < minn:
            minn = arr[idx][1]
            cnt += 1
        idx += 1

    print(cnt)