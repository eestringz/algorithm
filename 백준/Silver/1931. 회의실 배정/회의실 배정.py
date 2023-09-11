N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = arr[0][1]
for i in range(1, N):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]

print(cnt)