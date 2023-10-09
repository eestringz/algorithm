from collections import deque

def bfs():
    dty = [-1,0,1,0]
    dtx = [0,1,0,-1]
    while q:
        yy,xx = q.popleft()
        for i in range(4):
            dy = yy + dty[i]
            dx = xx + dtx[i]
            if dx<0 or dy<0 or dx>M-1 or dy> N-1: continue
            if arr[dy][dx] == 0:
                arr[dy][dx] = arr[yy][xx] + 1
                q.append([dy,dx])


M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i,j])

bfs()

flag = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = 1
            break

if flag:
    print(-1)
else:
    mx = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > mx:
                mx = arr[i][j]
    print(mx-1)