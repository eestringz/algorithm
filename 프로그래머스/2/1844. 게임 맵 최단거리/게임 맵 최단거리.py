from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque([(0, 0, 1)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        y, x, cnt = q.popleft()
        
        if y == n - 1 and x == m - 1:
            return cnt
        
        for dy, dx in directions:
            yy, xx = y + dy, x + dx
            
            if yy < 0 or xx < 0 or yy > n - 1 or xx > m - 1: continue
            if visited[yy][xx] != 1 and maps[yy][xx] != 0:
                visited[yy][xx] = 1
                q.append((yy, xx, cnt + 1))
    
    return -1
     
