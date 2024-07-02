from collections import deque

n = int(input())
q = deque([])
for _ in range(n):
    n, m = input().split()
    q.append([n, int(m)])

while len(q) > 1:
    first = q.popleft()
    x = first[1]

    if (x - 1) % len(q) == 0:
        q.popleft()

    else:
        for _ in range((x - 1) % len(q)):
            q.append(q.popleft())
        q.popleft()

print(q[0][0])
