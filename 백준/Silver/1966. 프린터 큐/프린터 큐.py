from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    cnt = 0

    while q:
        mx = max(q)
        first = q.popleft()
        m -= 1

        if first == mx:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else:
            q.append(first)
            if m < 0:
                m = len(q) - 1