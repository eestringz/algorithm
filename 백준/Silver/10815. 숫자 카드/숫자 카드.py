import sys

input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
lst = list(map(int, input().split()))

for i in range(m):
    flag = 0
    s, e = 0, n - 1
    while s <= e:
        mid = (s + e) // 2
        if card[mid] == lst[i]:
            flag = 1
            break
        elif card[mid] < lst[i]:
            s = mid + 1
        else:
            e = mid - 1
    print(flag, end=' ')