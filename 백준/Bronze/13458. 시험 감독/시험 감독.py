n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in range(n):
    if lst[i] <= b:
        cnt += 1
    elif (lst[i] - b) % c == 0:
        cnt += (lst[i] - b) // c + 1
    elif (lst[i] - b) % c != 0:
        cnt += (lst[i] - b) // c + 2

print(cnt)