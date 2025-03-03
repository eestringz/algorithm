import sys

input = sys.stdin.readline

arr = [list(map(str, input().split())) for _ in range(5)]


def dfs(x, y, digit):
    if len(digit) == 6:
        result.add(digit)
        return

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, digit + arr[nx][ny])


result = set()

for row in range(5):
    for col in range(5):
        dfs(row, col, arr[row][col])

print(len(result))
