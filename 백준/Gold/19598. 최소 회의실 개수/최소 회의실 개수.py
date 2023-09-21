import heapq
import sys

input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    q.append(list(map(int, input().split())))
q.sort(key=lambda x: (x[0], x[1]))

heap = []
heapq.heappush(heap, q[0][1])

for i in range(1, n):
    if q[i][0] < heap[0]:
        heapq.heappush(heap, q[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, q[i][1])

print(len(heap))