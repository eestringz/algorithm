import sys, heapq

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    num, s, e = map(int, input().split())
    arr.append([s, e])
arr.sort(key=lambda x: (x[0], x[1]))

heap = []
heapq.heappush(heap, arr[0][1])
for i in range(1, n):
    if arr[i][0] < heap[0]:  # 시작시간이 heap의 top보다 더 작으면 heap에 추가.
        heapq.heappush(heap, arr[i][1])
    else:  # 시작시간이 heap의 top보다 크거나 같으면, heap의 top은 pop하고 새로운 종료시간을 추가.
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))