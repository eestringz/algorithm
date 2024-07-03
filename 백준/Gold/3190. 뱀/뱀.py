from collections import deque

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1

l = int(input())
turn = {}
for _ in range(l):
    x, c = input().split()
    turn[int(x)] = c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

xx, yy, dd = 0, 0, 0
time = 0
snake = deque([])

while True:
    snake.append((xx, yy))
    time += 1
    xx += dx[dd]
    yy += dy[dd]

    if xx < 0 or yy < 0 or xx >= n or yy >= n or arr[xx][yy] == 2:
        break

    if not arr[xx][yy]:
        i, j = snake.popleft()
        arr[i][j] = 0

    arr[xx][yy] = 2

    if time in turn:
        if turn[time] == 'D':
            dd = (dd + 1) % 4
        else:
            dd = (dd - 1) % 4

print(time)