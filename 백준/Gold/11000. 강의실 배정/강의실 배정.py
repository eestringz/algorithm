import heapq

n = int(input())
q = []
for _ in range(n):
    q.append(list(map(int, input().split())))

q.sort()

heap = []
heapq.heappush(heap, q[0][1])
for i in range(1, n):
    if q[i][0] < heap[0]:  # 강의실이 추가로 필요한 경우
        heapq.heappush(heap, q[i][1])  # 새로운 종료시간 추가
    else:  # 강의실이 추가로 필요하지 않는 경우
        heapq.heappop(heap)  # 기존 종료시간을 새로운 강의의 종료시간으로 갱신
        heapq.heappush(heap, q[i][1])

print(len(heap))