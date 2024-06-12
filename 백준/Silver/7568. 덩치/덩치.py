n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    ans.append(cnt + 1)

for i in ans:
    print(i, end=' ')