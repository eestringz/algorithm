import heapq
import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(N):
    ans += lst[i] * (N - i)
print(ans)