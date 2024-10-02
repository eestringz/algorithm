N = int(input())
cards = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

dic = {}
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for num in lst:
    if num in dic:
        print(dic[num], end=' ')
    else:
        print('0', end=' ')
