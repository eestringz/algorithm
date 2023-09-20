n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.reverse()
cnt = 0
for i in range(n - 1):
    if lst[i + 1] >= lst[i]:
        cnt += lst[i + 1] - lst[i] + 1
        lst[i + 1] = lst[i] - 1

print(cnt)