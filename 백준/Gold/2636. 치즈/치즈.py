from collections import deque


# 외부 공기를 탐색하여 치즈와 접촉한 부분을 녹이는 함수
def bfs(board, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]

    visited[0][0] = 1
    board[0][0] = 2
    cheese_cnt = 0  # 현재 남아있는 치즈 칸의 개수

    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            yy, xx = y + dy, x + dx
            if yy < 0 or xx < 0 or yy > n - 1 or xx > m - 1: continue
            if visited[yy][xx] != 1:
                visited[yy][xx] = 1
                if board[yy][xx] == 0:  # 공기라면 탐색 확장
                    q.append((yy, xx))
                elif board[yy][xx] == 1:  # 치즈라면 녹일 준비
                    board[yy][xx] = 0  # 치즈를 녹임
                    cheese_cnt += 1

    return cheese_cnt


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time, last_cnt = 0, 0

while True:
    cheese_cnt = bfs(board, n, m)  # 현재 치즈를 녹임
    
    if cheese_cnt == 0:  # 치즈가 모두 녹았다면 종료
        break

    last_cnt = cheese_cnt  # 모두 녹기 한 시간 전 치즈 칸 수 저장
    time += 1

print(time)
print(last_cnt)
