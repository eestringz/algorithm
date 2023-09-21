import sys

input = sys.stdin.readline
n, m = map(int, input().split())
q = [[] for _ in range(n + 1)]
for _ in range(m):
    k, s, e = map(int, input().split())
    if not q[k]:
        q[k].append(e)
        print('YES')
    else:
        if s < q[k][0]:
            print('NO')
        else:
            q[k][0] = e
            print('YES')