N, X = map(int, input().split())
lst = list(map(int, input().split()))

summ = sum(lst[:X])
ans = summ
cnt = 1
for i in range(N - X):
    summ += lst[i + X] - lst[i]
    if summ == ans:
        cnt += 1
    elif summ > ans:
        ans = summ
        cnt = 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(cnt)