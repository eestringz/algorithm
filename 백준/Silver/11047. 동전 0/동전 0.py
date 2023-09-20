import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    x = int(input())
    if x > k:
        continue
    else:
        coins.append(x)

cnt = 0
idx = -1
while k > 0:
    cnt += k // coins[idx]
    k %= coins[idx]
    idx -= 1

print(cnt)