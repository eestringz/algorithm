N = int(input())

dic = {}
for _ in range(N):
    str = input()
    if str in dic:
        dic[str] += 1
    else:
        dic[str] = 1

dic_lst = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(dic_lst[0][0])
