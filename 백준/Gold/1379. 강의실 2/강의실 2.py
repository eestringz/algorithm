import sys, heapq

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[2]))    # 시작 시간, 종료 시간을 기준으로 정렬

heap = []           # 강의 시간 우선 순위 배열
ans = [0]*(n+1)     # 강의실 번호를 저장할 배열

num = 1         # 강의실 번호
ans[arr[0][0]] = num
heapq.heappush(heap, [arr[0][2],num])       # [종료시간,강의실 번호] 추가

for i in range(1, n):
    # 새로운 강의실이 필요한 경우 -> 강의실 번호를 하나 늘려 heap에 추가
    if arr[i][1] < heap[0][0]:
        num += 1
        ans[arr[i][0]] = num
        heapq.heappush(heap, [arr[i][2], num])
    # 새로운 강의실이 필요 없는 경우 -> 끝난 강의를 pop 하고, 그 강의실 번호를 그대로 가져와서 heap에 추가
    else:
        temp = heapq.heappop(heap)
        ans[arr[i][0]] = temp[1]
        heapq.heappush(heap, [arr[i][2], temp[1]])

print(len(heap))
for i in range(1,len(ans)):
    print(ans[i])