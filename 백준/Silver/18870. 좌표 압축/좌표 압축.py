n = int(input())
lst = list(map(int, input().split()))
dic = {num: i for i, num in enumerate(sorted(set(lst)))}
for i in range(n):
    idx = dic[lst[i]]
    print(idx, end=' ')