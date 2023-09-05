def dfs(y, x):
    global size
    arr[y][x] = 0
    dty = [-1, 0, 1, 0]
    dtx = [0, 1, 0, -1]
    for i in range(4):
        dy = y + dty[i]
        dx = x + dtx[i]
        if dx < 0 or dy < 0 or dx > N - 1 or dy > N - 1: continue
        if arr[dy][dx] == 0: continue
        arr[dy][dx] = 0
        size += 1
        dfs(dy, dx)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            size = 1
            dfs(i, j)
            cnt += 1
            lst.append(size)

lst.sort()
print(cnt)
print(*lst, sep='\n')