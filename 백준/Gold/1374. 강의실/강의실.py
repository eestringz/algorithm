import heapq

n = int(input())
q = []
for _ in range(n):
    a, b, c = map(int, input().split())
    q.append([b, c])

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