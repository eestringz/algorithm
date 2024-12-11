from collections import deque

def solution(progresses, speeds):
    q = deque([])
    answer = []
    
    for i in range(len(progresses)):
        remaining = (100 - progresses[i]) / speeds[i]
        q.append(int(remaining) if remaining.is_integer() else int(remaining) + 1)
    
    while q:
        current = q.popleft()
        cnt = 1
        
        while q and q[0] <= current:
            q.popleft()
            cnt += 1
        
        answer.append(cnt)
    
    return answer
